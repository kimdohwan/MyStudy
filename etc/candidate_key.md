### 후보키(카카오 코딩테스트 2018)

-----



###### 문제 설명

## 후보키

프렌즈대학교 컴퓨터공학과 조교인 제이지는 네오 학과장님의 지시로, 학생들의 인적사항을 정리하는 업무를 담당하게 되었다.

그의 학부 시절 프로그래밍 경험을 되살려, 모든 인적사항을 데이터베이스에 넣기로 하였고, 이를 위해 정리를 하던 중에 후보키(Candidate Key)에 대한 고민이 필요하게 되었다.

후보키에 대한 내용이 잘 기억나지 않던 제이지는, 정확한 내용을 파악하기 위해 데이터베이스 관련 서적을 확인하여 아래와 같은 내용을 확인하였다.

- 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
  - 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
  - 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

제이지를 위해, 아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.

![cand_key1.png](https://grepp-programmers.s3.amazonaws.com/files/production/f1a3a40ede/005eb91e-58e5-4109-9567-deb5e94462e3.jpg)

위의 예를 설명하면, 학생의 인적사항 릴레이션에서 모든 학생은 각자 유일한 학번을 가지고 있다. 따라서 학번은 릴레이션의 후보 키가 될 수 있다.
그다음 이름에 대해서는 같은 이름(apeach)을 사용하는 학생이 있기 때문에, 이름은 후보 키가 될 수 없다. 그러나, 만약 [이름, 전공]을 함께 사용한다면 릴레이션의 모든 튜플을 유일하게 식별 가능하므로 후보 키가 될 수 있게 된다.
물론 [이름, 전공, 학년]을 함께 사용해도 릴레이션의 모든 튜플을 유일하게 식별할 수 있지만, 최소성을 만족하지 못하기 때문에 후보 키가 될 수 없다.
따라서, 위의 학생 인적사항의 후보키는 학번, [이름, 전공] 두 개가 된다.

릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때, 이 릴레이션에서 후보 키의 개수를 return 하도록 solution 함수를 완성하라.

##### 제한사항

- relation은 2차원 문자열 배열이다.
- relation의 컬럼(column)의 길이는 `1` 이상 `8`이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
- relation의 로우(row)의 길이는 `1` 이상 `20`이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
- relation의 모든 문자열의 길이는 `1` 이상 `8`이하이며, 알파벳 소문자와 숫자로만 이루어져 있다.
- relation의 모든 튜플은 유일하게 식별 가능하다.(즉, 중복되는 튜플은 없다.)

##### 입출력 예

| relation                                                     | result |
| :----------------------------------------------------------- | :----- |
| `[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]` | 2      |

##### 입출력 예 설명

입출력 예 #1
문제에 주어진 릴레이션과 같으며, 후보 키는 2개이다.

---

### 다른사람 코드(풀지 못함)

```python
from itertools import combinations

def solution(relation):
    n_col = len(relation[0])
    
    # 컬럼의 조합 경우의 수를 구해서 리스트에 담아준다
    candidates = []
    for i in range(1, len(n_col + 1):
        combination_i = combinations(range(n_col), i)
        candidates.extend(combination_i)
        # append 를 사용하게 될 경우 itertool 함수가 list 에 추가 된다. 
        # append 는 object 를 추가하는 것이고 extend 는 iterable object 의 element 를 추가하는 것이다. *중요
    
    # 위에서 구한 후보키 조합으로 <1> 데이터를 매칭 시킨 뒤, <2> 중복이 존재하지 않는 데이터 후보키를 final 에 넣어준다 
    n_row = len(relation)
    final = []
    for keys in candidates:
        tmp = []
        for item in relation:
            a = []
            for key in keys:
                a.append(item[key])
            tmp.append(tuple(a))  # <1>
    # for keys in candidates:
    #     tmp = [tuple(item[key] for key in keys) for item in relation]
        
        if len(set(tmp)) == n_row:
            final.append(keys)  # <2>
            
    # final 에 최소성을 만족시키기 위해 중복된 key 가 들어간 애들을 제거해준다.
    answer = set(final)  # why set()? discard() 를 사용하려고
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if set(final[i]) == set(final[i]).intersection(set(final[j])):
                answer.discard(final[j])
    
    return len(answer)
        


```

일단 풀이를 보고 따라서 하나씩 진행해보긴 했지만 다시 풀라고 못 풀거 같은 문제다.

문제를 풀이하기 위해선 combinations 와 set 을 자유자재로 다룰 수 있어야 한다. ```combination(range(5), 3)``` 이라면, 0부터 4까지의 숫자 중 3개를 뽑아 만들 수 있는 조합을 생성한다. set 은 교집합이나 합집합, 차집합 등을 지원한다. 

전체적인 문제 풀이 방식을 살펴보면, 

1. 컬럼의 갯수로 조합할 수 있는 모든 집합을 구한다.(candidates)

   - extend 와 append 의 차이점은 iterable object 를 다루기 위해 꼭 필요하다

2. 구한 candidates 의 key 에 데이터 값을 대입한 후, 중복된 데이터를 제거한다.

   - key 값에 데이터를 대입하는 방식이 꽤나 까다롭다. list comprehension 으로 작성하면,
       ```python
       for keys in candidates:
           tmp = [tuple(item[key] for key in keys) for item in relation]
       ```
       다음과 같이 굉장히 간단하지만 풀어서 작성하려면 꽤나 어렵다. 연습을 많이 해봐야한다.

   - set 을 이용해 중복된 항목 제거
       ```
       # tmp, set(tmp) 를 비교한 출력
       -----keys =  (0,) 

       [('100',), ('200',), ('300',), ('400',), ('500',), ('600',)]

       {('600',), ('100',), ('500',), ('300',), ('400',), ('200',)} 데이터 중복 제거 후 

       -----keys =  (1,) 

       [('ryan',), ('apeach',), ('tube',), ('con',), ('muzi',), ('apeach',)]

       {('muzi',), ('con',), ('tube',), ('apeach',), ('ryan',)} 데이터 중복 제거 후 

       -----keys =  (2,) 

       [('music',), ('math',), ('computer',), ('computer',), ('music',), ('music',)]

       {('computer',), ('math',), ('music',)} 데이터 중복 제거 후 
       ```

   

3. 이 때 문제의 조건인 최소성을 만족시키기 위해 중복된 키가 들어간 경우를 또다시 제거해줘야한다.

   - ```[(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]``` 의 형태에서 최소성을 만족시키면 ```{(0,), (1, 2)}``` 가 된다. 
   - remove(a) 를 사용하면 a 가 없을 경우 에러가 나서 set() 의 discard(a) 를 사용한다.(인덱스와 .get() 의 차이와 유사)

   

### 다른사람 코드 2

```python
def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):  # 2^n-1(조합의 갯수)연산을 비트연산자로 실행함
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)  # 여기엔 문자열을 이어붙인 각 record 값이 들어오게됨

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)
```



비트 연산자를 통해 푼 코드인데 사실 잘 모르겠다 계속 변수 확인과 이래저래 알아보려고했지만 제대로 이해가 가 않는다. 나중에 다시 보기위해 남긴다.