### Brunch RSS Feed(개인 프로젝트)



### 개요

- 브런치 웹사이트(https://brunch.co.kr/)에 업데이트되는 최신글들의 RSS Feed 를 생성해주는 서비스

- 생성된 RSS Feed url 을 Feed 프로그램에 추가하여 브런치 글 구독 가능

- Feed 종류 : 검색어, 작가

- URL : https://www.idontknow.kr

- 프로젝트 동작 (사용한 Feed 구독 프로그램(웹): feedly)

  - 검색어 '커피' 입력 시 Feed URL 생성한 View

    ![Image](https://github.com/kimdohwan/MyStudy/blob/master/project/images/brunch/search.png)

    

  - 생성된 Feed

    ![Image](https://github.com/kimdohwan/MyStudy/blob/master/project/images/brunch/feed.png)

    

  - feedly 에서 생성된 Feed 를 구독하기

    ![Image](https://github.com/kimdohwan/MyStudy/blob/master/project/images/brunch/feedly.png)

    

  - 동작 영상 : [작가 검색](https://youtu.be/m4htPBcDcng) / [키워드 검색](https://youtu.be/1qhyNqZItJI)

- 도식화

  크롤링 속도 문제로 인해 lambda 사용하지 않도록 배포된 상태

  Django - [crawler.py](https://github.com/kimdohwan/Brunch-RSS-Feed/blob/master/app/articles/utils/crawling/crawler.py)로 크롤링 수행함

  ![Image](https://github.com/kimdohwan/Project/blob/master/blueprint_brunch.png)

### 진행 내용

- ##### RSS Feed 생성을 위한 크롤링 작업 

  - Selenium
    - Javasciprt 로 글 목록(검색 결과)을 불러온 후, `최신순` button click을 위해 사용
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

- [블로그](https://devdoh.tistory.com/59)

---

### 트러블 슈팅

- ##### 트러블 슈팅 1 : Celery 를 통해 백그라운드 작업 수행하기

  - 문제 상황은 무엇인가?

    - 웹사이트에서 Feed 생성을 위한 글을 크롤링하는 시간이 매우 오래 걸림(7초 이상)

  - 무엇이 문제일까?

    - 가장 큰 문제는 웹사이트에서 javascript 에서 글을 로딩하는 시간(총 5초 가량)
    - 특히 키워드 검색의 경우, 기본적으로 로드되는 '정확도' 순서가 아니라 '최신순으로' 정렬시켜야 하기 때문에 최신순 버튼을 따로 눌러줘야 하는 지연시간이 크다.
    - 크롤링 지연으로 인해 피드 생성 버튼을 누른 후, 한참이 걸려서 Feed URL 을 보여준다.

  - 어떻게 시간을 줄일 것인가? / 어떻게 빨리 결과(Feed URL)을 반환할 것인가?

    - 데이터베이스 자체에 접근할 수 있다면, 쿼리 최적화와 같은 방식으로 시간을 줄일 수 있다. 또는 Brunch 에서 제공해주는 API가 있다면, 그 또한 해결법이 될 수 있다.

      하지만 데이터베이스에 접근할 수도, 카카오에서 제공해주는 API에는 Brunch 관련 API가 당연히 없다. 그러므로 javascript 를 로딩시키는 시간을 줄이는 것은 불가피하다.

      그래서 생각한 것이 Celery 이다. 시간이 오래걸리지만 그 시간을 단축할 수 없는 작업을 백그라운드로 작업하게끔 할 수 있기 때문이다. Django에서 Celery를 활용하는 방법은 여러 블로그와 공식문서를 통해 어렵지 않게 익힐 수 있었다. 

      사용자가 '파이썬' 이라는 검색어를 입력하게되면, ```https://idontknow.kr/feeds/keyword/파이썬/```이라는 Feed URL을 리턴해주도록 하였다. 그리고 그동안 백그라운드에서는 Celery worker 와 redis 에서 '파이썬' 이라는 검색 결과에 해당되는 Brunch 웹사이트의 글들을 크롤링하게 된다. 

   - 개선 결과는? 

      - Celery 를 통핸 백그라운드 작업으로 인해, 크롤링 작업 시간 자체는 그대로이지만 Feed URL을 리턴해주는 시간 자체는 크게 단축되었다. 

        Celery 사용 전 : 7초 이상 

        Celery 사용 후 : 약 2~3초

        2-3초 라는 시간은 사용자가 입력한 검색어의 결과가 존재하는지 알아보는 시간이다. 예를 들어 'alsdfjlesijfaaselifj' 와 같은 존재하지 않는 검색어를 입력했을 경우까지 Feed URL 을 리턴해 줄 수 없기때문에, 검색결과가 존재하는지까지의 판단하는 작업 시간이 필요하다. 이 작업이 2-3초 가량 소요된다.

        원하는 결과만 빠르게 얻을 수있게 하고, 시간이 오래 걸리는 작업은 백그라운드에서 수행하도록 구현한 좋은 경험이 되었다. 

- ##### 트리블 슈팅 1-1 : asyncio 를 사용한 비동기 처리

  - 문제 상황 및 문제 파악은 트러블슈팅 1과 동일

  - Celery 를 사용한 방식은 크롤링 작업 자체의 시간을 단축시키는 것이 아니라, 그저 백그라운드에서 수행하게끔 하는 방식이다. 하지만 asyncio 와 aiohttp 를 통해 비동기 요청 구현으로 크롤링 작업 자체의 시간을 단축시켜보았다.

  - 동기적 / 비동기적([asyncio 포스팅](https://github.com/kimdohwan/MyStudy/blob/master/etc/asyncio.md))

    - 기본적으로 Django 는 비동기적 방식으로 동작한다. 5개의 URL 에 대해 Request 와 Response 를 그림과 같이 차례대로 수행한다.

      하지만 Python 의 genarator 를 기반으로 작동하는 asyncio 모듈을 사용하여 코드작성을 해주면, 비동기적인 방식의 코드 수행을 가능하게 해준다. 단, async 나 await 와 같은 asyncio 모듈이 실행되는 코드에서 작동되는 함수들 또한 asyn를 기반으로 작동해야 한다는 조건이 따른다. 

      aiohttp 는 비동기적으로 http 요청/응답을 수행하게 해주는 asyncio 라이브러리이다. 이를 활용하여 크롤링할 글이 10개 존재할 경우, http Request 를 10개의 URL 에 보낸다. 그리고 Response 가 도착한 순서대로 크롤링 작업을 수행하게 된다. 

  - ayncio 적용 후, 개선 결과는?

    - 10개의 Request를 기준으로, asyncio 를 사용한 후, 2~3초 걸리는 상세 페이지 크롤링 작업에서 약 1.5초 가량의 속도 향상을 이루었다. 10개밖에 안되는 작은 표본이기에 시간 단축은 그리 크지 않았지만 100개의 표본으로 진행해보니 더 큰 시간 단축이 일어나는 것을 확인하였다. 

  - asyncio 를 사용하여 Python/Django 에서 비동기적인 처리방식을 구현은 다양한 방식으로 응용가능하여, aiohttp 와 같은 HTTP 작업 뿐만아니라 다양한 작업을 지원하는 라이브러리가 있다. 

  

  





