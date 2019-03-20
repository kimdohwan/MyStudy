
json(base.json)을 이용해서  secret은 깃 제외 폴더,  
셋팅에는 불러오는 과정 적어둬서 로컬의 json파일이 있을 때만 시크릿 키를 획득할 수 있게 셋팅  

# - RDS  

### RDS 생성  
- postgresql 선택  
- 설정  
  - DB인스턴스 식별자, 마스터 사용자 이름, 마스터 암호  
  (마스터 사용자 이름과 암호 꼭 잘 기억하기)  
  - 기본 VPC 보안그룹 사용(미리 생성해놓은 보안그룹, default 지우기)  
    인바운드 설정 시, DB관련된 설정은 '내 IP'로 설정하는거 기억!
  - 퍼블릭 엑세스 가능  
  - DB 이름 설정
- 생성

### RDS 터미널로 접속  
- ```psql --host=<end point 복사> --user=<사용자 이름> --port=5432 postgres```  
  - 여기서 나는 에러(비밀번호가 뜨지 않는 경우)  
    보안그룹에 inbound 설정에 규칙 추가해주기  
- 접속 ok sql문으로 데이터 확인하자  


### json파일로 RDS 설정 보관  
> {  
  "DATABASES": {  
    "default": {  
      "ENGINE": "django.db.backends.postgresql",  
      "HOST": "엔드포인트",  
      "POST": 5432,  
      "USER": "유져",  
      "PASSWORD": "비밀번호",  
      "NAME": "ec2_deploy_rds"  
    }  
  }  
}    

### 터미널 창에서 RDS DB 적용하기  
- ```export DJANGO_SETTING_MODULE=config.settings.dev```
  터미널의 env 안에 있는 DJANGO_SETTING_MODULE 변수 저렇게 설정


# - IAM

### 생성
- 사용자 추가    
  - 프로그래밍 방식 엑세스(key를 이용해 터미널로)   
  - 콘솔 엑세스(인터넷 창)
- 암호 설정
  - 기존 정책 직접 연결  
  s3 검색 후 AmazonS3FullAccess 선택  
- 비밀 엑세스 키와 암호 기록  
  - 이 때만 볼 수 있음!!
  - 폴더 생성: ```mkdir ~/.aws```   
  - credentials 파일: ```vi credentials``` 만들고 아이디, 키 적어주기  
  >  [fc-8th-s3]  
aws_access_key_id = ddddd  
aws_secret_access_key = sdfdskfjhk

  - config 파일: ```vi config```
  > [default]  
region = ap-northeast-2  
output = json
