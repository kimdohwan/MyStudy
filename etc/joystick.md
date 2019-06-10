### 조이스틱(프로그래머스)

조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

```
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
```

예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

```
- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
```

만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

##### 제한 사항

- name은 알파벳 대문자로만 이루어져 있습니다.
- name의 길이는 1 이상 20 이하입니다.

##### 입출력 예

| name   | return |
| :----- | :----- |
| JEROEN | 56     |
| JAN    | 23     |

---

### 다른사람 풀이(풀지 못함)

```python
def solution(name):
    answer = 0

    move_list = []
    for i in range(0, len(name)):
        move = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        move_list.append(move)

    left_end_idx = 0
    right_end_idx = 0
    for i in range(1, len(move_list)):
        if move_list[i] > 0:
            right_end_idx = i
            if left_end_idx == 0:
                left_end_idx = i

    answer = min(right_end_idx, len(move_list) - left_end_idx)
    for move in move_list:
        if move > 0:
            answer += move

    return answer
```

- 풀지 못한 이유

  일단 문제를 잘 못 이해했다. '이전 알파벳' 커서의 행동을 왼쪽으로 이동하는 것이 아니라 무조건 마지막 위치로 움직이는 줄 알았다. 문제를 똑바로 읽지 않아서 접근이 완전히 잘못되었다.

- 문제를 해결하는 2단계

  - 첫번째: 각각의 알파벳 변환에 필요한 횟수 계산

    - 아스키 코드와 최솟값 연산으로 계산 가능(이부분은 스스로 구현함)

  - 두번째: 커서 움직임 계산(```A```의 위치에 따라서)

    - 커서를 오른쪽으로 움직일 것인가, 왼쪽으로 움직일 것인가에 관한 문제

      왼/오 움직임 계산 후 최소값 연산을 해주면 된다. 왼/오 움직임 계산이 관건이다.

    - 움직임 계산

      왼/오 의 end point 를 계산해주는 작업이다. 

      'AABCC' 의 왼쪽 end point 는 B([2])가 되고 오른쪽 end point 는 C([4])가 된다.

      왼쪽으로 이동하는 횟수:

      ​	 ```len('AABCC') - left_end_point``` 5 - 2 = 3 이 된다.(A -> C -> C -> B)

      오른쪽으로 이동하는 횟수: 

      ​	```right_end_point``` 4가 된다.(A -> A -> B -> C -> C)

---

### 풀이 참조해서 내가 다시 작성한 코드

```python
def solution(name):
    answer = 0
    ascii_A, ascii_Z = ord('A'), ord('Z')
    
    l_end = 0
    r_end = None
    
    for i, s in enumerate(name):
        if not s == 'A':
            # 알파벳 계산
            ascii_s = ord(s)
            start_from_A = ascii_s - ascii_A
            start_from_Z = ascii_Z - ascii_s + 1
            answer += min(start_from_A, start_from_Z)
    		
            # 커서 움직임 계산
            r_end = i
            if l_end == 0:
                l_end = i
                
    answer += min(r_end, len(name) - l_end)
    return answer

# 3가지 경우 - 테스트케이스 업데이트로 인해 3번 경우 추가시켜줘야 할듯?
# 1. 오른쪽으로만 갈 경우
# 2. 왼쪽으로만 갈 경우
# 3. 오른쪽 갔다가 왼쪽 가는 경우
```

일단 enumerate 를 사용하여 for loop 를 한번만 사용하도록 했고, ascii_A 와 같은 변수를 미리 선언하여 for loop 안쪽에서 최대한 함수 스택을 줄여보았다. 프로그래머스에서 테스트케이스가 업데이트되어서 현재 이 코드로 통과되지 않는다. 아마도 주석 3번 경우에 해당하는 부분이 추가된 듯하니 이 부분을 나중에 수정해봐야할 것 같다. 
