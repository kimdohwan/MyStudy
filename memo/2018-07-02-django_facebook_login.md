
---
---
페이스북의 로그인으로 user 생성과 로그인을 대신할 수 있다  
facebook login process라고 검색, 이미지로 이해하자  



developers.facebook.com 을 참고  
facebook login 문서와 그래픽 API를 사용한다.  
login.html파일에서 시작해 views.py로 이어진다.
```python
urls.py
    path('facebook-login/', views.facebook_login, name='facebook-login'),
```

```html
login.html

<div>
    <!--페이스북 로그인 페이지로 보냄, 클라이언트 id와 리다이렉트 uri를 포함-->
    <!--페이스북 다이얼로그로 auth요청을 보내는 과정이다.-->
    <!--클라이언트 아이디는 내 앱으로 부터 요청을 보내는 것을 의미 -->
    <!--리다이렉트는 로그인 후 돌아오는 페이지, request에 code를 받아서 돌아온다-->
    <!--code는 view함수에서 진행됨 -->
    <a href="https://www.facebook.com/v3.0/dialog/oauth?
  client_id=631395940565915
  &redirect_uri=http://localhost:8000/members/facebook-login/&scope=email,public_profile" class="btn btn-primary">페이스북 로그인</a>
</div>
```

```python
views.py
def facebook_login(request):
    # 템플릿에서 첫번째 과정을 거친 후 request에서 code 전달됨(authentication code)
    # 전달받은 인증 코드를 사용해서 access token 을 얻음
    code = request.GET.get('code')
    url = 'https://graph.facebook.com/v3.0/oauth/access_token'
    params = {
        'client_id': settings.FACEBOOK_APP_ID,
        'redirect_uri': 'http://localhost:8000/members/facebook-login/',
        'client_secret': settings.FACEBOOK_APP_SECRET_CODE,
        'code': code,
    }
    # access code를 받기위해 다시 요청을 보냄
    # 클라이언트 아이디, 리다이렉트 uri에 덧붙여
    # 시크릿 코드와 전달받은 인증 코드를  params에 덧붙여 보낸다
    response = requests.get(url, params)
    # 제이슨은 텍스트로 전달된 엑세스 토큰을 딕트 형태로 변환 시켜주는 파이선 모듈이다
    # 제이슨을 통해서 토큰을 변수에 할당
    response_dict = json.loads(response.text)
    response_dict = response.json()
    access_token = response_dict['access_token']

    # 얻은 토큰을 통해 해당 사용자 고유의 user_id를 받을 수 있다
    # 얻은 토큰을 디버그 해주는 과정
    url = 'https://graph.facebook.com/debug_token'
    params = {
        'input_token': access_token,
        'access_token': f'{settings.FACEBOOK_APP_ID}|{settings.FACEBOOK_APP_SECRET_CODE}',
    }
    # response에는 기본적인 유져 프로필과 같은 사항이 담기게 된다
    response = requests.get(url, params)


    # 그래픽api를 통해서 추가적으로 필요한 정보를 탐색해본 후 얻어온다
    # 여기서부터는 그래픽 api 사용법 문서를 참고해서 진행함
    # email과 같이 그래픽에서 얻어오지 못한 것은 주소창의 스코프를 이용한다??
    url = 'https://graph.facebook.com/v3.0/me'
    params = {
        'access_token': access_token,
        'fields': ','.join([
            'id',
            'name',
            'first_name',
            'last_name',
            'picture',
        ])
    }
    # 필드의 정보를 담은 응답을 얻는다
    response = requests.get(url, params)
    response_dict = response.json()

    facebook_user_id = response_dict['id']
    first_name = response_dict['first_name']
    last_name = response_dict['last_name']
    url_img_profile = response_dict['picture']['data']['url']

    # 받은 정보를 get_or_create를 이용해 새로 유져를 생성한다
    # 여기서 - if문을 사용하지 않고 작성
    #       - default값으로 지정해주는 방법:
    #             get 에는 username만 사용되고 defaults로
    #             지정된 값들은 create 할 때 사용된다
    user, user_created = User.objects.get_or_create(
        username=facebook_user_id,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
        },
    )
    login(request, user)
    return redirect('index')
```
