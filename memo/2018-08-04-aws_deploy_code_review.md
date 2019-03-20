
it's a description how deploy code work.  
- diagram
```
├── app
│   ├── config
│   │   ├── __init__.py
│   │   ├── settings
│   │   │   ├── base.py
│   │   │   ├── dev.py
│   │   │   ├── __init__.py
│   │   │   └── production.py
│   │   ├── urls.py
│   │   └── wsgi
│   │       ├── dev.py
│   │       ├── __init__.py
│   │       └── production.py
│   ├── db.sqlite3
│   ├── manage.py
│   └── rewards
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── build.py
├── deploy.sh
├── Dockerfile
├── Dockerfile.base
├── Dockerfile.production
├── Pipfile
└── Pipfile.lock
```  

### docker image(Dockerfile.base) 생성
- build.py
  1. ```pipenv lock -r > requirements.txt```  
    - docker container 에는 pipenv 를 사용하지 않으므로 pipfile 에서 package를 뽑아내서 requirements.txt 로 생성
  2. ```docker build -t <image name>:<tag name> -f <build file>```   
    - docker image 생성(build), 여기서 <build file> 은 Dockerfile.base 라고 가정



- Dockerfile.base
  - build.py 에서 생성된 requirements.txt 를 복사 및 pip install -r 실행
  - Dockerfile.base build 후에 requirements.txt 는 build.py 에서 delete 처리  
```python
COPY                ./requirements.txt /srv/
RUN                 pip install -r /srv/requirements.txt
```  

### 생성된 Dockerfile.base 를 dockerhub image 로서 활용한다    
- dockerhub
  Dockerfile 에서 parent image 로서 Dockerfile.base 를 dockerhub 으로부터 받아오도록 한다   
  1. ```docker tag teamproject:base dosio0102/teamproject:base```  
  - dockerhub 으로 보낼 name 지정, image 생성(dockerhub repository name 과 일치시켜야한다)  

  2. ```docker push dosio0102/teamproject:base```
  - 로그인이 되어있는 상태라고 가정(로그인된 계정의 repo 로 push)

### eb 에서 실행될 도커 파일
- Dockerfile
  1. ```from        dosio0102/teamproject:base```  
  - parent image 로 base 파일 사용  
  (Dockerfile build 할 때 base image 또한 같이 build 된다)
  2. ```ENV         DJANGO_SETTINGS_MODULE      config.settings.${BUILD_MODE}```  
  - BUILD_MODE 를 production 으로 설정(production 으로 설정된 명령어는 생략)   
  3. nginx 설정해주기  
```
RUN    cp -f   /srv/project/.config/${BUILD_MODE}/nginx.conf \
                  /etc/nginx/nginx.conf && \
          cp -f   /srv/project/.config/${BUILD_MODE}/nginx_app.conf \
                  /etc/nginx/sites-available/ && \
          ln -sf  /etc/nginx/sites-available/nginx_app.conf \
                  /etc/nginx/sites-enabled/
```  
  - nginx.conf: 기본 설정파일  
  - nginx_app.conf: 연결 될 site 에 관한 설정
    - sites-enabled: 실제 운영되는 site 설정
    - sites-available: 넣어둔 설정을 sites-enabled 로 링크 시켜주는 역할
  4. supervisor 설정해주기  
  ```RUN             cp -f   /srv/project/.config/${BUILD_MODE}/supervisor.conf \
                        /etc/supervisor/conf.d/```
  - supervisor.config: nginx 와 uwsgi 를 실행유지 시켜주는 설정파일  
    ```command=uwsgi --ini /srv/project/.config/dev/uwsgi.ini```   
    ```commnad=nginx```
  5. ```EXPOSE          7000```  
  - docker container 에서 사용할 port(열어두는)
  - nginx_app.conf 에서 ```listen 7000;``` 으로 설정되어있으므로  docker container dml 7000번 포트로 들어오는 request 를 열어줘서 nginx 가 사용할 수 있게 해준다  
  6. ```supervisord -n``` supervisor 실행

### nginx -> (socket) -> uwsgi -> (config.wsgi.production) -> django   
- socket: nginx 와 uwsgi 를 연결
- config.wsgi.production: uwsgi 와 django 를 연결   
  1. config.wsgi.production  
    - DJANGO_SETTINGS_MODULE 을 config.settings.production 으로 설정  
  2. config.settings.production  
    - django app 에 사용될 설정들 적용(DB, INSTALLED_APP, ALLOWED_HOST 등등)
