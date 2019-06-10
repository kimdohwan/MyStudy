## AWS 배포시 나타나는 무한 로딩 문제 사례 

---

##### 보안그룹 설정 누락

- RDS
  - 사용중인 AWS RDS 의 보안그룹에 EB or EC2 보안그룹 추가 필요
  - 현상: Timeout 응답 메시지 
- EB(SecurityGroup)
  - 80/443 추가
- EB(LoadBalancer)
  - https 요청을 받는 경우, 로드 밸런서에 리스너 추가 해준 후 로드밸런서 보안그룹에 https(443) 추가

##### Nginx 설정 오류

- EC2 의 Nginx 설정에서 Docker container 로 forwarding 을 시켜주는 설정 오류 시
  - 사례: ```http```로 들어오는 요청을 ```https```로 넘겨주는 설정을 ```.ebextensions```에 설정한 상태에서 Docker container 에 ssl 인증서 처리를 해주지 못한 상황
  - 현상: 무한 로딩 후 http 응답 코드나 메시지없이 연결 실패하게 됨

