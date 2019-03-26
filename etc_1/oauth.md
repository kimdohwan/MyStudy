OAUTH

1.사용자가 페이스북으로 로그인을 시도한다

2.사용자는 페이스북 홈페이지에서 로그인과 권한 사용 동의를 한다.

  - 이때 클라이언트는 scope(사용할 정보,권한), redirect, client_id 를 함께 제공

3.리소스 서버(페이스북)은 등록된 redirect 로 code 를 보내준다.

4.클라이언트는 받은 code, client_id, socket 을 서버에 보낸다 

5.리소스 서브는 확인 후 access_token 을 보내준다

6.이제 api 를 사용하는 request 를 보낸다

