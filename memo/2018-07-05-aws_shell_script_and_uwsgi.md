
서버 동작 설명(강사님)
```
1. /static/ -> STATIC_ROOT 경로에서 파일을 리턴하도록 설정
2. 그 외 URL요청은 -> Django가 처리 후 Response하도록




- WebServer(Nginx), WSGI(uWSGI)
Browser -> EC2 -> WebServer -> (static)   -> STATIC_ROOT
                            -> (dynamic)  -> WSGI -> Django

- runserver
Browser -> EC2                            -> Django(runserver
                                                    :8000)

- uWSGI
Browser -> EC2            -> uWSGI:8000   -> Django

- Nginx, uWSGI
Browser -> EC2 -> Nginx   -> uWSGI:80     -> Django

```

- ```manage.py collectstatic```  
장고 sitepackage의 static파일인 admin과 우리가 만들어준 static파일을 STATIC_ROOT로 모아준다.  -webserver에서 wsgi(그리고 장고)를 거치지 않고 바로 탐색할 경로가 STATIC_ROOT  



config.settings  
```python
STATIC_DIR = os.path.join(BASE_DIR, 'static')
ROOT_DIR = os.path.dirname(BASE_DIR)

STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
# 스태틱 루트를 지정해야 ./manage.py collectstatic 명령어 가능
```

 받아 적은 내용  
- 스태틱파일(이미지 등)은 runserver(django)에서 불러오는 것 보다 webserver에서 곧바로 /static/abc.jpg와 같이 접근하는 것이 더 효율적이고 최적화 되어있다고 함.  


- 웹서버에서 static file에 접근할 수 있게 해주는 로직이 필요.  
- /manage.py collectstatic 을 통해 장고에서 스태틱파일을 통합.  
(STATICFILES_DIR에는 django site package admin의 static을 자동 포함)
- 통합해주는 이유:  
웹서버는 장고처럼 static의 경로가 2개가 있는 경우(sitepackage, 내 api)에는 static을 추적하지 못하기 때문이다. 한마디로 '웹서버의 static file 경로 지정'
