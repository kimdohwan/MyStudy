기능 개발(프로그래머스)
---

#### 문제 설명  
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항  
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.  
작업 진도는 100 미만의 자연수입니다.  
작업 속도는 100 이하의 자연수입니다.  
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.  
입출력 예
  
|progresses|speeds|return|
|------------|--------|--------|
|[93,30,55]|[1,30,5]|[2,1]|

입출력 예 설명  
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.  
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.  
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.  

따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.  


---

#### 내 풀이
```python
import math

def solution(progresses, speeds):
    answer = []
    required_dates = []
    for progress, speed in zip(progresses, speeds):
        required_dates.append(math.ceil((100 - progress) / speed))
    while required_dates:
        required_date = required_dates.pop(0)     
        if not answer or required_date > last_date:
            answer.append(1)
            last_date = required_date
        else:
            answer[-1] += 1
    return answer
```  
변수명 잘못 지은느낌이다.  
숫자 올림을 하고 싶어서 ceil 을 썼다.(모듈을 최대한 사용하지 않으려했지만...)  

#### 다른사람 풀이(map, lambda)
```python
from math import ceil

def solution(progresses, speeds):
    # ---- 주목 ----
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    print(daysLeft)
    # -------------
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList
```  
나는 for 문과 append 를 사용해서 구한 남은 날짜 계산을 저 코드에서는 map, lambda, range 를 통해 구현했다.  
lambda 로 계산식을 작성했고 map() 의 인자로 lambda 함수와 range(lambda 의 인자로 동작)를 넣어줬다.  

#### 다른사람 풀이(math 모듈 사용하지 않고 숫자 올림)  
```python
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
        print(dir(-70 / 30))
    return [q[1] for q in Q]
```  
ceil() 함수를 사용하지 않고 올림을 할 수 있는 방법이다. 파이썬 나눗셈에서 몫을 구할 때, 항상 그래프의 왼쪽에 해당되는 값이 몫이 된다.  
예를 들어 2.5 의 그래프 왼쪽에 위치한 정수인 2가 몫이 되며,
음수의 경우, -2.5 라면 그래프 상에서 왼쪽에 위치한 정수 -2 가 몫이 된다.  
C, JAVA 의 경우 -3 이 몫이 되므로 파이썬의 특징으로 기억하고 프로그래밍 지식으로 혼동하지 말자.  
아무튼 이점을 이용하면 float 형이 나오든 int 가 나오든 내가 원하는 방식으로 값을 올림 할 수 있다.  

또한 이 코드에서는 반복문을 한번만 사용했다. 남은 날짜와 return 할 기능 갯수를 리스트로 묶어 한꺼번에 append 시켜줬다는 점이 특이하다.