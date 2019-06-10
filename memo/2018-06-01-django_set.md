Django Setting
```
1. 폴더 생성
>django
  >django_프로젝트이름

2. git 설정
>git init
>.gitignore 파일 생성
  vi .gitignore(django, python, mac, linux, pycharm all, git)

3. virtualenv 설정
>pyenv virtualenv 3.6.5 네임
>pyenv local 네임

4. pycharm interpreter 가상환경 설정
>경로:/home/kimdohwan/.pyenv/versions/네임/bin/python

5. django install
>pip install django~=1.11.0

6. myblog 시작(manage.py 등 파일 생성시키기)
>djanfo-admin startproject mysite

7. 디렉토리 이름 변경
    djangogirls-tutorial/
        mysite/                    <- Django프로젝트 관련 코드 컨테이너 폴더
            manage.py
            mysite/                <- 이 Django프로젝트의 설정 관련 패키지
                __init__.py
                settings.py


      a. Django코드 컨테이너 폴더의 이름을 app으로 변경
          리팩터 파일 체크 풀고 실행
      b. Django프로젝트 설정 패키지의 이름을 config로 변경
          리팩터 둘다 체크하고 실행


    djangogirls-tutorial/    <- 이 프로젝트의 컨테이너 폴더 (Root폴더)
        app/                    <- Django프로젝트 관련 코드 컨테이너 폴더
            config/                <- Django프로젝트의 설정 관련 패키지
                settings.py

        .gitignore                <- Django프로젝트(애플리케이션) 코드와 관계없지만
        .git/                        프로젝트를 위해 필요한 파일/폴더들
        requirements.txt

8. source root 폴더 지정해주기
>app파일을 루트폴더로 지정(__init__파일이 없는데도 패키지 폴더로 지저되는 app-> 파이썬의 특징)
  바꿔주고 나면 패키지 표시가 사라짐

9.requirements.txt 생성
>pip freeze > requirements.text
  장고 버젼 및 설치 패키지 기록(다른 사용자 or 나중을 위해)



```
-manage.py  
이 스크립트로 다른 설치작업 없이 컴퓨터에서 웹서버 실행  
사이트 관리를 도와주는 역할


-settings.py  
웹사이트 설정


-urls.py  
ulrresolver가 사용하는 패턴목록을 포함  
사용자가 입력한 url을 어떻게 처리(안내)할지 안내해줌
```
Browser -> (request) -> Server -> Django application   
-> urlresolver  
    ->    view1 -> (process) -> (response) -> Server -> Browser  
        view2
        view3
```
