
새로 적용된 모델 필드가 잘 적용되지 않을 때

./manage.py showmigration  

./manage.py migrate NAME zero  

./manage.py migrate   

zero로 돌려 준 후에 다시 migrate하자   

위 과정 없이 migrations 폴더의 파일만 삭제할 경우  
제대로 테이블의 정보가 셋팅되지 않게되는 문제 발생함


지속적으로 에러나는 부분인만큼 신경써줄 것
