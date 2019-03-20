
(1) AWS 홈페이지에서  EC2 새 인스턴스 생성  
- 인스턴스 시작
  1. Amazon Machine Image(AMI)  
    Ubuntu 16.04 SSD 선택  
  2. 인스턴스 유형 선택  
  3. 인스턴스 세부정보 구성  
  4. 스토리지 추가  
  5. 태그 추가  
  6. 보안 그룹 구성
    새 보안그룹 생성: 보안 그룹 이름, 설명  
    (생성 안하면 default, 작동 안함)  
  7. 인스턴스 시작 검토  
    기존 키 페어 선택 또는 새 키 페어 생성  
      새 키 생성시 꼭 download 해야한다  
      (여기서 못하면 끝)  

(2) 다운받은 키 파일(.pem) .ssh 폴더로 이동  
- ```mv ~/Downloads/fc-doh.pem ~/.ssh```  


(3) 키 파일 권한 관리자 읽기모드로 변경  
- ```chmod 400 fc-doh.pem```  


(4) ssh 명령어로 aws서버에 접속  
  - ```ssh -i /path/my-key-pair.pem ec2-user@ec2-198-51-100-1.compute-1.amazonaws.com```  
    ssh -i(identify) file_path(key) username(ex: ubuntu, ec2-user)@public_DNS  


(5) 가상환경 설정(포스트 'aws pipenv,pip setting' 참고)  


(6) 장고 프로젝트 로컬에 생성  


(7) aws에 로컬 프로젝트 복사  
  - ```scp -i ~/.ssh/fc-doh.pem \\n-r ~/projects/deploy \\ubuntu@ec2-52-79-201-93.ap-northeast-2.compute.amazonaws.com:/home/ubuntu/project```  
    - deploy 안쪽의 파일들을 project폴더로 복사(deploy파일이 들어가는 것이 아니다. deploy안쪽의 파일(ex:django_tutorial)이 project폴더 안쪽으로 들어간다.  
    - 역슬래쉬(\)로 구분해서 입력,항목 안빠뜨리게 주의  
    - ```-r``` 옵션과 ubuntu@(유져네임) 명령어 빠뜨리기 쉬우니 주의  


(8) aws 서버에 장고 설치 및 가상환경 설정(장고설치 되서 scp되었을 수도 있다)  
  1. 가상환경 설정  
    ```pipenv shell```  
  2. 장고 설치  
    ```pipenv install django```  


(9) runserver 실행  
  1. settings.py 안쪽에 ALLOWED_HOST 설정  
  (charm이 설치 안되어 있으므로 vi 로 수정 가능)  
  ```'localhost', '.amazonaws.com', '127.0.0.1'```  
  2. aws 홈페이지에서 보안그룹 편집  
  - 인바운드 편집 -> 규칙 추가
    - 유형: 사용자 지정 TCP 규칙  
    - 포트범위: 8000  
    - 소스: 위치무관  
    - 설명: runserver(알아서)
  3. 0:8000 붙여서 runserver 실행  
  ```./manage.py runsever 0:8000```
