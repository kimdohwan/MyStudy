

#### 기본적으로 nginx는 설치 후 명령어 입력하면 80번 포트로 바로 연결된다  
  - 무한 로딩되면서 welcome page가 뜨지 않는 경우
    - 보안그룹에서 inbound 셋팅에 80번 포트 잘 추가되었는지 확인  
    (이것 때문에 시간 많이 썼다, nginx에 기본적으로 세팅된 80번포트를  
      aws에 추가시켜주지 않으면 아무런 동작이 없는게 당연)

#### error 분석(nginx 연결 ok, uwsgi와 연결 x, bad gateway)

  - 에러 메시지(/var/log/nginx/error.log)  
  ```[crit] 19347#19347: *30 connect() to unix:///tmp/app.sock failed (2: No such file or directory) while connecting to upstream,```  
  - 소켓파일 연결에 실패한 상태  
  uwsgi에는 app.socket 이라고 입력했고  
  nginx에는 app.sock 이라고 오타를 낸 경우

#### 502 bad gateway(uwsgi install 버젼이 낮아서 생긴 문제!!해결완료)
  - uwsgi 에러(```uwsgi --ini <file>```)
    ```
    *** Operational MODE: single process ***
    *** no app loaded. going in full dynamic mode ***
    -> 노 앱 로디드 부분은 uwsgi 설정파일이 틀렸다는 것(uwsig.ini 파일 확인해볼 것)
    *** uWSGI is running in multiple interpreter mode ***
    !!!!!!!!!!!!!! WARNING !!!!!!!!!!!!!!
    no request plugin is loaded, you will not be able to manage requests.
    you may need to install the package for your language of choice, or simply load it with --plugin.
    -- unavailable modifier requested: 0 --
    ```
  - nginx 로그 에러(/var/log/nginx/error.log, tail -f error.log)  
    - ```upstream prematurely closed connection while reading response header from upstream```  
    이 경우 파이썬 관련 플러그인이 제대로 설치되지 않았기 때문?  


#### ```supervisord -n```(실행 중 나오는 에러)  
  ```2018-07-09 02:41:07,647 INFO gave up: uwsgi entered FATAL state, too many start retries too quickly```  
  uwsgi 가 제대로 실행되지 않은 error(경로 오타 주의)


#### ```no python application```  
  - 이 경우 파이썬 어플리케이션(ex: pipenv로 설치해주는 것들)이 없다는 것  
  - ```tail -f error.log``` 명령어가 아닌 전체를 보여주는 ```cat```으로 에러구문 찾아볼 것  
  (ex: no module storages >> 파이썬 앱(storages)이 제대로 빌드 안된 경우)

#### ```internal server error```
  - 안쪽에서 에러났다 -->> 장고 에러일 가능성  
  - 해결 방법: 런서버로 확인해보기
  - uwsgi.log 확인해보기(no app loaded, No module 등등)

### [supervisor(링크)](http://supervisord.org/)
  ini 파일을 대신 수행하면서 프로세스를 관리해주는 프로그램  
  사용법: ```supervisord -n``` 다른 건 링크 잠고
