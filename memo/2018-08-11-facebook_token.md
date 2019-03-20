

페이스북 로그인 강사님 메모

```python1
Django SessionAuthentication
    Browser -> username/password -> authenticate()
        -> 성공시 session_id값을 django_sessions테이블에 저장
            -> 브라우저에게 SET-COOKIE헤더로 session_id값 전달
            -> 브라우저는 이후 해당 쿠키를 계속해서 Request에 담아서 보냄
            -> 서버는 session_id값이 포함되어 있는 경우 특정 유저를 인증


Token Authentication
클라이언트 -> authenticate
    -> 성공시 Django DB에 특정 User에 대한 Token을 저장
    -> Response에 저장한 Token의 key값을 보내줌
    -> 클라이언트는 이후 HTTP Request Header의 'Authorization'항목에
        "Token <key>"를 담아서 요청
    -> 서버는 Authorization헤더의 값이 'Token'으로 시작할 경우, DB에 저장된 Token목록을 검사, 일치하는 유저가 있으며 Token이 유효할 경우 인증된것으로 처리



-- 로그인
- 유저 입장 (iOS또는 프론트엔드 애플리케이션을 사용중) - 회원가입은 되어있음
1. 로그인 페이지에 접속
2. username/password(로그인정보) 입력
3. 전송
4. (과정은 모르지만) 계속 로그인이 유지되고 있다

- 클라이언트 입장
1. 유저가 입력한 정보를 사용해서 HTTP Request를 서버로 보냄
2. 특정 Token이 돌아올 것이라고 가정, Response에서 토큰값을 추출
3. 토큰값을 자신의 특정 저장공간에 보관
4. 이후의 Request에는 보관하고 있는 Token값을 Authorization헤더에 'Token <값>'으로 담아 전송, 이렇게 하면 인증이 유지될것이라 기대

- 서버 입장
1. (클라이언트에서 인증정보를 보냄) 인증정보에 해당하는 유저가 실제로 있는지 검사 (authenticate)
    (인증에 성공한경우)
        -> 인증에 성공한 User에 해당하는 Token값을 없으면생성, 있으면 그걸 사용
    (인증에 실패한경우)
        -> raise AuthenticationFailed()를 실행, 401 HTTP응답을 돌려줌
2. 생성한 Token값을 Response
3. 이후 Token을 받은 클라이언트가 매번 'Authorization'헤더에 해당 값을 담아 보낼것으로 기대
4. (Authorization헤더에 특정 값이 담긴 Request를 받았을 때)
== 아래는 자동 ===
4-1. 헤더에 담긴 'Token값'이 유효한지(해당 내용이 Token테이블에 있는지)검사
        (성공시) -> request.user에 특정 User가 할당
        (실패시) -> request.user에 AnonymousUser가 할당

-> members.apis.AuthToken <- APIView
    POST요청이 왔을 경우 위의 로직을 작성
    URL: /api/members/auth-token/
        다 되면 Postman작성, 테스트

    INSTALLD_APPS에 'rest_framework.authtoken'추가 후 진행
    시작전에 'auth-token'브랜치 생성 및 체크아웃 후 진행
```

```python1
Django를 사용한 페이스북 로그인
1. 페이스북 로그인 버튼 클릭
2. 페이스북 페이지로 이동, 사용자가 로그인
3. application으로 redirect되며 'code'값을 GET parameter로 받음
4. code를 access_token과 교환

4-1. 클라이언트가 access_token을 사용해서 사용자정보를 받아오고,
        추가 정보를 입력받음 -> 사용자정보와 추가정보들을 전부 서버로 전송
4-2. 클라이언트가 access_token만 서버로 전송
----------클라이언트-----------


5-1. 받아온 정보들로 application에 회원가입
5-2. access_token으로 유저의 페이스북 정보를 받아옴
        이후 페이스북에서 받은 유저정보로 application에 회원가입

-> 서버에서는 Token을 돌려줌 (DRF로그인 유지 토큰)



로그인을 유지시키기
1. 서버에서 받아온 Token이 쿠키의 'token'키값에 저장되어있음
2. 클라이언트가 처음 로드 될 때 마다 해당 키를 사용해 HTTP Header의 인증을 만든 상태로 유저 정보를 받아오는 API를 실행
3-1. API호출에 성공하면 (token이 유효하면)
    전송받은 User정보를 사용해 화면을 렌더링 (@@로 로그인 중)
    로그인 버튼을 가림
3-2. API호출에 실패하면 (token이 유효하지 않음)
    로그인 버튼을 보여줌
```
