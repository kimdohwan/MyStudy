AWS Route53, ACM

- rout53  
아마존에서 제공하는 DNS 서비스이다. 보통 도메인을 한 ip 에 붙일 수 있는데 우리가 사용하는 eb 의 경우엔 동적으로 생성되는 ec2 가 여러개 존재 할 수 있기 떄문에 load balancer 쪽으로 도메인을 붙여야 한다. route53 은 도메인을 ip 가 아닌 load balancer 로 붙일 수 있게 하는 서비스이다. 구입한 도메인 호스팅 홈페이지에서 네임서버 변경을 통해 route53 의 record set 을 추가해주면 된다. route53 설정 시 alias 항목에 eb, load balancer 두개중 loadbalancer 로 설정해주는 것이 https 인증서를 붙이는데 더 편하다 
- acm   
ssl 인증서를 제공해주는 aws 서비스  
생성 후 eb loadbalancer 보안그룹에 https 를 추가해줘야 https 로 오는 요청을 받을 수 있다.
- nginx_app.conf  
nginx servername 에 내 도메인드를 추가해준다