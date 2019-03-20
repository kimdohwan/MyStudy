AWS EB Setting

eb init 과 eb create 를 헷갈리지 말자 
1. eb init  
	eb cli project 환경을 구성하는 단계라고 할 수 있다. ec2 를 만드는 과정 이전에 eb cli 의 전반적인 환경설정을 해주는 작업이라고 생각하면 된다. region, credential, application name, platform(docker), codecommit, keypair 등 과 같은 요소를 설정해주며 해당 프로젝트에 .elasticbeanstalk 라는 폴더 안쪽에 eb cli 에 관련된 config.yml 파일이 생성된다. 

2. eb create   
	실질적으로 ec2 가 생성되고 eb 를 통해 배포가 되는 단계이다. create 를 완료하면 배포가 자동적으로 실행되는데 이 과정에서 error 가 나게되면 eb deploy 를 통해서 다시 배포를 진행할수 있다. 

3. eb deploy --staged  
	git 과 eb는 서로 연동되어서 git 에 commit 된 내용만 배포가 가능하다. 이 때 배포에 필요한 파일이지만 git에 올리면 안되는/싫은 파일이 있을 수 있다. 예를 들어 aws eb key 의 경우 git 에 commit 되어 올라가게 된다면 보안상 큰 문제가 된다. 이런 경우를 위해 git add 만 되어있는 상태, staged 라는 옵션을 이용한다. staged 되어있는 파일들은 배포하되 git 에는 staged 되어있는 파일이 commit 되지 않기 때문에 유용하게 쓰일 수 있다.
	배포 과정에서 나는 ERROR massege 에는 꽤 세세한 정보가 담겨있으니 꼭 잘 챙겨보도록 하자.
	특히 배포 에러 발생 시  도커 파일 셋팅과 관려된 aws 문서를 잘 봐야 한다. EXPOSE 셋팅이라던지 등등.

4. eb ssh  
	우리가 실행하고 있는 eb ec2 로 접속 할 수 있는 명령어이다.
	배포과정에서 발생하는 에러는 /var/log/eb-activity.log 에서 확인할 수 있으며 해당 path 는 배포 에러 시 출력되는 메시지에서 확인가능하다.
	eb ssh 로 접속한 ec2 에서 내가 만들어준 도커로 들어가서 에러로그를 볼 수있다. sudp docker ps 명령어를 이용해 도커 컨테이너로 접근가능하며 그 다음과정은 로컬에서 진행한 방법과 동일하다. 만약 내 docker container 안쪽에서 uwsgi, nginx error log 가 없다면 ec2 nginx 에러로그를 살펴봐야 한다

5. Dockerfile EXPOSE 셋팅   
	eb Dockerfile 셋팅에 꼭 포함되어야 하는 설정으로 local 에서 docker run 할때 설정해주는 -p 부분에 해당한다. docker container 가 실행될 때 사용할 port 를 지정해 줄 수 있다. 만약 EXPOSE 7000 으로 설정을 추가해준다면 내가 실행한 도커 컨테이너는 port 7000 번을 이용해 nginx 에게 request 를 넘겨준다. 
	이때 중요한 설정은 nginx_app.conf 에 들어가는 listen 설정인데, 만약 이 설정을 EXPOSE 에 적어준 port 번호와 일치시켜주지 않으면 niginx 가 요청을 받을 수 없게 된다. 그러므로 꼭 EXPOSE 설정과 nginx 설정을 함께 추가시켜주도록 하자. 이 부분은 nginx, uwsgi log 에서 확인할 수 없는 부분이니 만약 놓치게 된다면 삽질시간이 많이 늘어날 수도 있다.

5. .ebextensions  
	배포 전, 후 시점을 선택해서 실행하고 싶은 명령어(collectstatic, migrate)를 수행해 줄 수 있다. 또한 파일을 생성하는 등 여러 기능이 존재한다. hook/appdeploy/post 경로에 migrate 쉘 스크립트 파일을 생성하면 배포 후 자동으로 migrate 명령어를 수행시킬 수 있다.