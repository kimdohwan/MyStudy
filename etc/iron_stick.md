#### 쇠막대기

---



###### 문제 설명

여러 개의 쇠막대기를 레이저로 절단하려고 합니다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자릅니다. 쇠막대기와 레이저의 배치는 다음 조건을 만족합니다.

```
- 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있습니다.
- 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓습니다.
- 각 쇠막대기를 자르는 레이저는 적어도 하나 존재합니다.
- 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않습니다.
```

아래 그림은 위 조건을 만족하는 예를 보여줍니다. 수평으로 그려진 굵은 실선은 쇠막대기이고, 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향입니다.

![image0.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/dbd166625b/d3ae656b-bb7b-421c-9f74-fa9ea800b860.png)

이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있습니다.

```
(a) 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 '()'으로 표현합니다. 또한 모든 '()'는 반드시 레이저를 표현합니다.
(b) 쇠막대기의 왼쪽 끝은 여는 괄호 '('로, 오른쪽 끝은 닫힌 괄호 ')'로 표현됩니다.
```

위 예의 괄호 표현은 그림 위에 주어져 있습니다.
쇠막대기는 레이저에 의해 몇 개의 조각으로 잘리는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘리고, 이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘립니다.

쇠막대기와 레이저의 배치를 표현한 문자열 arrangement가 매개변수로 주어질 때, 잘린 쇠막대기 조각의 총 개수를 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- arrangement의 길이는 최대 100,000입니다.
- arrangement의 여는 괄호와 닫는 괄호는 항상 쌍을 이룹니다.

##### 입출력 예

| arrangement            | return |
| :--------------------- | :----- |
| ()(((()())(())()))(()) | 17     |

##### 입출력 예 설명

문제에 나온 예와 같습니다.

---

#### 내 풀이

```python
def solution(arrangement):
    answer = 0
    stick_count = []
    before_i = ''
    for i in arrangement:
        if i == '(':
            stick_count.append(1)
        elif before_i + i == '()':
            stick_count.pop(-1)
            answer += len(stick_count)
            # 위코드로 바꾸기 전에는 for j in stack_count: 를 통해 모든 항목에 +1 진행했다
        else:
            answer += stick_count.pop(-1)
            # 위에서 for 문을 사용안하고 len()를 사용하기 때문에 
            # 여기서 pop() 에 -1 로 인덱스 지정을 할 필요가 없어졌다 
            # 위코드 수정 후 pop() 으로 고치면 더 좋았을 것이다 
        before_i = i
    return answer

# ( 이 나오면 +1 하고 ) 이 나오면 pop[-1] 및 answer += 한다.
# 레이져 식별은 ( 이 나오면 무조건 +1이다 다음 )이면 pop[-1] 하고 리스트에 전부 1씩 더해준다.
```

한창 고민했다. 처음엔 쇠막대기의 갯수와 레이져 갯수를 파악해야 하는 것으로 접근했지만 아니었다.  

() 의 규칙과 return 해야하는 숫자를 끼워 맞춰보자 라는 생각으로 다시 접근해보았다.  

( 이 나오면 쇠막대기라고 판단하고 레이져로 판단되면 쇠막대기를 줄였다. 코드 하단의 주석은 처음에 문제를 풀려고 한 방식이며 len(stick_count) 방식으로 바꾼 후 시간초과 에러를 해결할 수 있었다.

#### 다른사람 풀이(True/False, list 사용 없음)

```python
def solution(arrangement):
    answer = 0
    stack = 0
    laseron = False
    for p in arrangement:
        if p == '(':
            laseron = True
            stack += 1
        else:
            if laseron==True:  # 레이져 '()' 에 해당됨
                answer += stack-1  # 레이져로 +1 시킨걸 -1 해주고 잘린 갯수만큼 +
                laseron=False  # 레이져 닫아줌
            else:
                answer += 1
            stack -= 1  
            # ')' 이면 레이져든 막대기든 -1 필요
            # 막대기: 스택 없앰
            # 레이져: 잘못올린 막대기 스택 없앰

    return answer
```

멋진 코드다. for loop 에서 처음에 하는 조건 검사도 2가지(나는 3가지)이고 무엇보다도 레이져 처리를 True/False 로 한 부분이 신기하다. 리스트를 사용하지 않았고 오로지 숫자 카운트를 통해 해결했다.   

내 코드의 경우 처음의 의도는 해당되는 막대기의 분리되는 갯수를 각각 리스트에 보관 후 막대기 끝에 다다르면 pop()으로 처리하려고했다. 하지만 중첩 for loop 로 인해 테스트를 통과하지 못했고 그 후 len() 을 이용해 테스트를 통과했다. 하지만 len() 으로 코드수정 후에 사실 리스트를 사용할 필요가 없는 코드가 되었다. 그점을 눈치채지 못했다. 

#### 고쳐본 코드(list 사용없이)

```python
def solution(arrangement):
    answer = 0
    stick_count = 0
    before_i = ''
    for i in arrangement:
        if i == '(':
            stick_count += 1
        else:
            if before_i + i == '()':
                answer += stick_count - 1
            else:
                answer += 1
            stick_count -= 1
        before_i = i
    return answer
```

