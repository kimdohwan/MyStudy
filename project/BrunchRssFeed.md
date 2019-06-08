### Brunch RSS Feed(개인 프로젝트)



### 개요

- 브런치 웹사이트(https://brunch.co.kr/)에 업데이트되는 최신글들의 RSS Feed 를 생성해주는 서비스
- 생성된 RSS Feed url 을 Feed 프로그램에 추가하여 브런치 글 구독 가능
- Feed 종류
  - 검색어, 작가
- URL
  - https://www.idontknow.kr
- 프로젝트 동작 영상
  - 작가 검색: https://youtu.be/m4htPBcDcng  
  - 키워드 검색: https://youtu.be/1qhyNqZItJI
  - 사용한 Feed 프로그램(웹): feedly

### 진행 내용

- ##### RSS Feed 생성을 위한 크롤링 작업 

  - Selenium
    - Javasciprt 로 글 목록(검색 결과)을 불러오기 위해 사용
    - EB Docker container 에서 동작하기 위해 별도의 Chrome driver 및 Headless Chrome 설치 필요(배포 시 Dockerfile 에서  Install 수행)
  - Celery
    - 오래걸리는 크롤링 작업을 백그라운드에서 수행
    - Broker : Redis 사용(AWS Elasticache instance)
    - 주기적인 Feed Update 를 위해 Celery beat 작업 수행(등록된 키워드와 작가의 글을 크롤링하는 작업)
  - Python Library
    - requests
      - Selenium 을 통해 얻은 글 목록 HTML 에서 각각의 글 정보를 얻은 후, 상세페이지에서 저장될 글 내용에 해당되는 TAG 를 뽑기위해 사용
    - asyncio
      - aiohttp : 여러개의 글 상세 페이지에 대한 http 요청 작업을 비동기적으로 수행하기위해 사용

- ##### RSS Feed 생성 및 URL 제공

  - Django Feed framework

    - Django 내에서 RSS Feed 를 생성할 수 있는 Library

    - Feed Class 를 상속받아 커스터마이징 수행

    - 동작 방식 

      1. ```urls.py``` 를 통해 Feed Class View 실행(Parameter : keyword / writer)

      2. 전달된 Parameter 에 해당되는 글(Article Object)을 DB 로부터 불러옴

      3. 글(Article Object)의 제목, 내용 등의 데이터를 사용해 Feed View 생성

- ##### AWS EB 배포 및 AWS 기능 활용

  - Elastic Beanstalk(Docker application)
    - 배포 스크립트( ```deploy.sh```)를 사용해 eb deploy 실행
    - 배포 시 migrate 실행을 위해 Beanstalk Hook 기능을 사용
  - Route53, ACM 
    - 도메인 연결 및 SSL 인증서 발급
  - S3, Elasticache(redis), RDS(postgresql)

- ##### Sentry

  - 배포 서버의 에러 관리를 위해 ```config.settings.production``` 환경에 설정
  - 사용중인 Integration : Django, Celery, AioHttp 

### 후기

- 트러블 슈팅
  - 





