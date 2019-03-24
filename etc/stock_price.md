### 주식 가격
---
문제 설명  
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항  
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

입출력 예  

| prices |	return |
| ------------- | ------------- |
|[1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |

입출력 예 설명

1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.  
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.  
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.  
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.  
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.  

---
정답
```python
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    for i in range(len(prices)):
        p = prices.popleft()  # 큐
        answer.append(0)  # 스택?이지만 구지 필요하지는 않다
        if prices:  # 마지막에 1개 일 경우를 거르기위해
            for j in prices:  # 크기 비교 및 기간 평가
                answer[i] += 1
                if p > j:
                    break
    return answer
```  
prices 의 마지막 아이템은 return 이 0 이 되어야 한다는 점이 포인트다.  
deque 를 통해 하나씩 값 비교를 하는데 가장 해맷던 부분은 2번째 for 문 안쪽의 break 부분이다. break 만 응용할 생각을 했다면 쉽게 풀렸을텐데 break 를 생각못하고 if 로만 간단하게 구현하려다보니 많이 꼬였다.  
더이상 +1 연산이 필요하지 않을 때 break 를 이용해 멈춰주는 부분만 잘 구현하면 나머지는 어렵지 않다.
