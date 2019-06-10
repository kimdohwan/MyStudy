### EB create 실행 시 IAM permission Error 해결하기

---

#### 문제 상황

aws 계정을 새로 만든 상태로 eb 배포를 진행하기 위해 eb create 를 하던 중, 다음과 같은 에러 발생

```Describe your new note here.
Printing Status:
2019-05-13 11:16:51    INFO    createEnvironment is starting.
2019-05-13 11:16:53    INFO    Using elasticbeanstalk-ap-northeast-2-348718493386 as Amazon S3 storage bucket for environment data.
2019-05-13 11:17:14    INFO    Created target group named: arn:aws:elasticloadbalancing:ap-northeast-2:348718493386:targetgroup/awseb-AWSEB-TGBE799ODJOS/206a73cab621d890
2019-05-13 11:17:14    INFO    Created security group named: sg-0ca4aa5035c40afb0
2019-05-13 11:17:30    ERROR   Stack named 'awseb-e-386qseptfi-stack' aborted operation. Current state: 'CREATE_FAILED'  Reason: The following resource(s) failed to create: [AWSEBV2LoadBalancer, AWSEBSecurityGroup]. 
2019-05-13 11:17:30    ERROR   Creating load balancer failed Reason: API: elasticloadbalancingv2:CreateLoadBalancer User: arn:aws:iam::348718493386:user/EB_Full is not authorized to perform: iam:CreateServiceLinkedRole on resource: arn:aws:iam::348718493386:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing
2019-05-13 11:17:30    ERROR   Creating security group named: awseb-e-386qseptfi-stack-AWSEBSecurityGroup-1L3VV4Q2YHUQ4 failed Reason: Resource creation cancelled
2019-05-13 11:17:32    INFO    Launched environment: testeb-dev. However, there were issues during launch. See event log for details.```
```

IAM 권한에 EBFullAccess 를 설정했는데도 불구하고 로그밸런서 생성에서 permission error 발생 



#### 해결 방법/원인

- 해결방법: IAM 정책에 로드밸런서를 생성과 관련된 권한을 추가해줘야함(인라인 추가)

```{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeAccountAttributes"
            ],
            "Resource": "*"
        }
    ]
}
```

- 원인: brandnew 에 해당하는 계정엔 loadbalancer 가 생성되어있지 않다. EBFullAccess 권한에  CreateServiceLinkedRole 권한이 포함되지 않은 상태로 로드밸런서 생성을 진행하게되고 이로인해 permission error 가 발생한다. EBFullAccess 의 경우, 이미 로드밸런서가 생성된 후에 진행한다고 가정하여 해당 권한이 포함되어있지 않았다.
- 해결 방법 url: https://github.com/terraform-aws-modules/terraform-aws-eks/issues/103



#### 권한 정책 사용하는 법

에러를 다시 읽어보자

```2019-05-13 11:17:30    ERROR   Creating load balancer failed Reason: API: elasticloadbalancingv2:CreateLoadBalancer User: arn:aws:iam::348718493386:user/EB_Full is not authorized to perform: iam:CreateServiceLinkedRole on resource: arn:aws:iam::348718493386:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing```

- 메시지 중 해결 방법을 알려주는 두가지 구문
  - ```to perform: iam:CreateServiceLinkedRole``` 
    - perform 은 Action 에 들어갈 내용을 의미 
  - ```on resource: arn:aws:iam::348718493386:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing```
    - resorce 는 Resource 에 들어갈 내용을 의미 

#### 고칠점/느낀점

에러구문을 보고 직접 권한 코드를 작성하는 시도를 하지 않았다. IAM 권한의 Statement, Effect, Action, Resource 에 대해 대충 읽을줄만 알고 작성해본 적이 없었기에 에러 메시지에 모든 해결 방법이 나와있음에도 몇시간을 낭비했다. 뭐가 됫든 에러 메시지를 토대로 직접 해결해보려고 노력했어야 했는데 구글 검색에 너무 의존하였다. 

