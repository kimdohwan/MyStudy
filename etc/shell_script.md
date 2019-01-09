## ec2 shell script 작성하기

ec2 에 접속, 프로젝트 폴더를 삭제하고 다시 복사하는 과정을 shell script 로 작성

```
#!/usr/bin/env bash

IDENTITY_FILE="$HOME/.ssh/aws-ec2-doh.pem"
USER="ubuntu"
HOST="ec2-52-78-184-164.ap-northeast-2.compute.amazonaws.com"
PROJECT_DIR="$HOME/Yolo/Project"
SERVER_DIR="/home/ubuntu/Project"

ssh -i ${IDENTITY_FILE} ${USER}@${HOST} rm -rf ${SERVER_DIR}

scp -q -i ${IDENTITY_FILE} -r ${PROJECT_DIR} ${USER}@${HOST}:${SERVER_DIR}

```


---


VENV_PATH: ec2 에 접속 후 cd 명령어를 통해 프로젝트 폴더로 이동, ```pipenv --venv``` 를 통해 프로젝트에서 사용하는 가상환경의 경로를 얻는다. ```pipenv shell``` 명령어를 사용하지 않고도 해당 폴더에 들어가서 ```pipenv --venv``` 를 입력하면 해당 프로젝트의 가상환경 경로가 나온다는 사실을 기억하자.  
PYTHON_PATH: ```manage.py``` 를 실핼하기 위해서 필요한 파이썬 경로를 얻어온다. 가상환경의 bin/python 폴더가 해당 프로젝트를 실행시키는 파이썬에 해당되며 ```./manage.py runserver``` 와 ```python manage.py``` 는 같은 작동을 하게된다.

```
#!/usr/bin/env bash

IDENTITY_FILE="$HOME/.ssh/aws-ec2-doh.pem"
USER="ubuntu"
HOST="ec2-52-78-184-164.ap-northeast-2.compute.amazonaws.com"
PROJECT_DIR="$HOME/Yolo/Project"
SERVER_DIR="/home/ubuntu/Project"

# ssh 연결
CMD_CONNECT="ssh -i ${IDENTITY_FILE} ${USER}@${HOST}"

# ssh 연결 후, server project 로 이동, 가상환경 경로를 담음
VENV_PATH=$(${CMD_CONNECT} "cd ${SERVER_DIR} && pipenv --venv")

PYTHON_PATH="${VENV_PATH}/bin/python"
echo $PYTHON_PATH

RUNSERVER_CMD="nohup ${PYTHON_PATH} manage.py runserver 0:8000"
echo $RUNSERVER_CMD

${CMD_CONNECT} "cd ${SERVER_DIR}/app && ${RUNSERVER_CMD}"

echo "End"
```

