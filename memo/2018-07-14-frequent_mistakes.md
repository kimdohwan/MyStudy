
### RDS inbound ip 추가해주기(Elasticbeanstalk instance)  
- 물리적인 공간(집, 학원)의 보안그룹 IP말고도 EC2 서버 컴퓨터 또한 DB에 접근하게 됨.
- EC2 인스턴스의 보안그룹의 Elasticbeanstalk의 그룹이 2개 생성되어 있다. 그 중 각각의 그룹설명을 살펴보자
  - Elastic Beanstalk created security group used when no ELB security groups are specified during ELB creation
  - SecurityGroup for ElasticBeanstalk environment.  
    -->> 이게 ElasticBeanstalk의 서버 환경에 해당(도커 환경 아님)
- RDS inbound 추가하기
  - ElasticBeanstalk 환경의 그룹 ID를 인바운드 규칙의 소스에 입력
  - type: PostSQL, port: 5432 source: eb env group id

### +=, = 구별하기
- settings.py 를 Convert To Python Package 한 경우  
  INSTALLED_APPS 에 추가 시 실수  
  - GOOD  
  ```
  INSTALLED_APPS += [  
  'storages',  
  ]
  ```
  - BAD
  ```
  INSTALLED_APPS = [  
      'storages',  
  ]
  ```  
  - error message
>  "INSTALLED_APPS." % (module, name)
RuntimeError: Model class django.contrib.contenttypes.models.ContentType doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.  

### RDS inbound ip 추가해주기  
- runserver 실행 시 밑에서 머물러있는 현상 발생  
>Performing system checks...  
System check identified no issues (0 silenced).  

### docker hub image 를 사용하는 경우  
- base 가 되는 image 가 update 되었는지 체크할 것  
