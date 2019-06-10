

#### django gmail setting  
- gmail 기본 셋팅
  1. IMAP 사용함 설정
  2. 보안수준 낮은 앱 허용
- settings.py  
```python1
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '메일주소'
EMAIL_HOST_PASSWORD = '비밀번호'
SERVER_EMAIL = '메일주소'
DEFAULT_FROM_MAIL = '아이디'
```  

- test 'send email' in shell_plus   
```python1
>>> from django.core.mail import EmailMessage
>>> email = EmailMessage('subject text', 'body text', to=['id@gmail.com'])
>>> email.send()
```

### url 설정
- POST 'signup/' : 회원가입 후 이메일 발송  
- GET 'activate/' : 인증 링크 클릭 시 user.is_active = True 로 활성화

### 회원가입 및 이메일 전송 API  

- api.py(view)
```python1
class UserList(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- serializer.py
```python1
class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.SlugField(max_length=12, min_length=1, allow_blank=False, write_only=True)
    nickname = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User

        fields = (
            'pk',
            'username',
            'password',
            'nickname',
            'img_profile',
        )

    def validate_password(self, value):
        if value == self.initial_data.get('password1'):
            return value
        raise ValidationError('(password, password1) 불일치')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            nickname=validated_data['nickname'],
            # img_profile=validated_data['img_profile'],
        )
        user.is_active = False
        user.save()

        message = render_to_string('user/account_activate_email.html', {
            'user': user,
            'domain': 'localhost:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
            'token': account_activation_token.make_token(user),
        })

        mail_subject = 'test'
        to_email = user.username
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        return validated_data
```  
- token.py
```python1
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )
account_activation_token = AccountActivationTokenGenerator()
```
- html 파일(이메일에 발송될 내용)
```python1
{ { user.nickname } } 님 링크를 클릭해 계정을 활성화 해주세요
http://{{ domain }}{ % url 'user:activate' uidb64=uid token=token % }
```

- api.py(view) 유져가 이메일 링크를 누르면 동작하는 부분
```python1
class UserActivate(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64.encode('utf-8')))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        try:
            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return HttpResponse(user.email + '계정이 활성화 되었습니다', status=status.HTTP_200_OK)
            else:
                return HttpResponse('만료된 링크입니다', status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(traceback.format_exc())
```
