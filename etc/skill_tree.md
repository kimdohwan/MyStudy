### 스킬트리
---
문제 설명  
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.  

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.  

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.  

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.  

제한 조건  
스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
스킬 순서와 스킬트리는 문자열로 표기합니다.  
예를 들어, C → B → D 라면 CBD로 표기합니다  
선행 스킬 순서 skill의 길이는 2 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.  
skill_trees는 길이 1 이상 20 이하인 배열입니다.  
skill_trees의 원소는 스킬을 나타내는 문자열입니다.  
skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.   

입출력 예  

| skill	| skill_trees | return |
|-------|-------------|--------|
| CBD	| [BACDE, CBADF, AECB, BDA] | 2 |

입출력 예 설명  
BACDE: B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트립니다.
CBADF: 가능한 스킬트리입니다.  
AECB: 가능한 스킬트리입니다.  
BDA: B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트리입니다.  
---
코드  
```python
# 내가 푼 코드
def solution(skill, skill_trees):
    answer = 0 
    for skill_tree in skill_trees:
        i = 0 
        for user_skill in skill_tree:
            if user_skill in skill:
                if user_skill == skill[i]:
                    i += 1
                else:  # 순서가 다르면 pass
                    break
        else:
            answer += 1            
    return answer
```  
위 코드의 경우 인덱스 체크를 위해 i 사용하였다. 또한 처음 풀었을 때는 for else 를 사용하지 않고 문제를 풀었기 때문에 변수 연산도 더 필요했다.   
밑 코드의 경우 list 를 새로 만들어 pop 을 통해(queue) 내가 추가한 인덱스 연산을 대신했다. 이 경우가 더 좋은코드 같으니 참고할 것. 또한 for else 도 중요한 부분.  
```python
# 다른 사람 풀이
def solution(skill, skill_trees):
    answer = 0 
    for skill_tree in skill_trees:
        l_skill = list(skill)
        for s in skill_tree:
            if s in skill:
                if s != l_skill.pop(0):
                    break
        else:
            answer += 1
    return answer

```