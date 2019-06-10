

### Serialization, Deserialization
- instance 를 serialize 시킨 후 stream 에 담긴 데이터를 다시 deserialize 하는 일련의 과정을 이해하자
- Stream objects(스트림 객체) -> 나중에 알아볼 것
  - 파이썬의 open() 내장함수를 사용하면 stream 객체를 반환한다. 이때 stream 객체는 문자열 stream 에 대한 정보를 얻거나 조작할 수 있는 method 와 attribute 를 가지고 있다.

```python
In [47]: r1 = Reward.objects.first() # Reward 오브젝트

In [48]: r1
Out[48]: <Reward: Reward object (2)>

In [49]: s1 = ReSerializer(r1) # 오브젝트를 serialize

In [50]: s1
Out[50]:
ReSerializer(<Reward: Reward object (2)>):
    id = IntegerField(read_only=True)
    no = IntegerField()
    category = CharField()
    company = CharField()

In [51]: s1.data # serialize 된 data 확인
Out[51]: {
'id': 2,
'no': 21901,
'category':
'스포츠·모빌리티',
'company': '와글리 (WAGGLY)'
}

In [52]: content = JSONRenderer().render(s1.data)
         # JSON 형식으로 렌더링

In [추가]: content  # JSON 형식의 데이터
Out[추가]: b'{   
"id":2,
"no":21901,
"category":"\xec\x8a\xa4\xed\x8f\xac\xec\xb8\xa0\xc2\xb7\xeb\xaa\xa8\xeb\xb9\x8c\xeb\xa6\xac\xed\x8b\xb0",
"company":"\xec\x99\x80\xea\xb8\x80\xeb\xa6\xac (WAGGLY)"
}'

In [53]: stream = BytesIO(content)

In [54]: stream
Out[54]: <_io.BytesIO at 0x7f20cbf0eeb8>

In [55]: data = JSONParser().parse(stream)
         # JSON 형식을 파이썬이 읽을 수 있게 parse

In [56]: data # 파이썬으로 읽을 수 있게 된 데이터
Out[56]: {'id': 2, 'no': 21901, 'category': '스포츠·모빌리티', 'company': '와글리 (WAGGLY)'}

In [57]: s2 = ReSerializer(data=data) # deserialization

In [58]: s2
Out[58]:
ReSerializer(data={'id': 2, 'no': 21901, 'category': '스포츠·모빌리티', 'company': '와글리 (WAGGLY)'}):
    id = IntegerField(read_only=True)
    no = IntegerField()
    category = CharField()
    company = CharField()

In [60]: s2.is_valid() # s2 의 데이터가 valid 한가?
Out[60]: True

In [61]: s2.validated_data # validation 검사 완료 된 데이터
Out[61]:
OrderedDict([('no', 21901),
             ('category', '스포츠·모빌리티'),
             ('company', '와글리 (WAGGLY)')])

In [62]: s2.save()
# Reward instance 로 deserializ?
# create 함수가 없으므로(ReSerializer 안쪽에) 생성 불가
# generics 같은 모델을 상속받으면 알아서 셋팅되어 있음
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-62-2042e7a4926b> in <module>()
----> 1 s2.save()

~/.local/share/virtualenvs/teamproject-21XHzuqQ/lib/python3.6/site-packages/rest_framework/serializers.py in save(self, **kwargs)
    212             )
    213         else:
--> 214             self.instance = self.create(validated_data)
    215             assert self.instance is not None, (
    216                 '`create()` did not return an object instance.'

~/.local/share/virtualenvs/teamproject-21XHzuqQ/lib/python3.6/site-packages/rest_framework/serializers.py in create(self, validated_data)
    167
    168     def create(self, validated_data):
--> 169         raise NotImplementedError('`create()` must be implemented.')
    170
    171     def save(self, **kwargs):

NotImplementedError: `create()` must be implemented.
```
