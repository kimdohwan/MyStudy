
### insertion sort(삽입 정렬)  
- insertion sort 는 bubble sort 와는 달리 앞쪽에서부터 값의 비교를 통해 재정렬을 이룸.
- insertion sort code(python)
```1
def insertion_sort(x):
    for i in range(1, len(x)):
        j = i - 1
        key = x[i]
        while x[j] > key and j >= 0:
            x[j+1] = x[j]
            j = j - 1
        x[j+1] = key
    return x
```
>### In  
a = [5, 4, 3, 2, 1]  
insertion_sort(a)  
print(a)  
### out  
[1, 2, 3, 4, 5]  

- 작동 원리  

  ##### 첫번째 for 문
  - for 문에서 range(1, len(x)) 를 순회한다.  
    list a 의 경우, range(1, 5) 를 가지며 i 값에 1, 2, 3, 4 의 값이 할당된다.  
  - j = i -1  
    j 는 i 에 -1 을 한 값으로 index 를 이용할 때 i 보다 한 칸 앞쪽의 값을 비교하기위해 지정해주는 변수이다.  
  - key  
    list의 i 번째 값을 할당한다.  
    크기비교를 해주는 값으로 while 문에서 고정된 값을 가진다.    

  ##### 안쪽 while 문 작동할 지 연산  
  - x[j] > key  
    list 의 j번째(i 보다 한칸 앞선 값이고 while 문 루프를 돌 경우 -1 씩 변경된다.) 값과 key(x[i]) 값을 크기비교하여 x[j] 값이 클 경우 while 문 작동  
  - j >= 0  
    while 문을 돌게 될 경우, j 의 값이 -1 씩 차감되므로 0 밑으로 내려갈 경우 while 문을 돌지 않게 된다.  

  ##### 안쪽 while 문 작동  
  - x[j + 1] = x[j]  
    while 문 루프를 돈다는 것은 바꿔줘야 할 값이 존재함을 의미.  
    x[j] 값이 key(x[i]) 값보다 크다면 재정렬이 이뤄져야 한다.  
    x[j+1] 에 x[j] 를 할당함으로써 더 큰 값인 x[j] 를 한칸 뒤쪽으로 할당(삽입)한다.
  - j = j - 1  
    할당이 완료 되었으므로 j 값을 차감시켜서 더 앞쪽의 값과 비교,연산을 진행할 수 있게 한다.  

  ##### 직접 안쪽에서 순서대로 일어나는 일을 집어보자.  
    - #### for loop i = 1 값을 가질 때, j = i - 1, key = x[i]    
    j = 0, key = x[1] (value 4 할당)  
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 5, key = 4 , j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[1] = 5, j = -1 할당.  
        j 가 0 보다 작으므로 while loop 종료.  
        a = [5, 5, 3, 2, 1]  
      - ##### for loop 하단, while loop 종료 후 x[j + 1] = key  
      x[0] = 4 값이 할당  
        a = [4, 5, 3, 2, 1]

    - #### for loop i = 2 값을 가질 때, j = i - 1, key = x[i]    
    j = 1, key = x[2] (value 3 할당)  
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 5, key = 3, j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[2] = 5, j = 0 할당.  
        j >= 0 이므로 while loop 지속.  
        a = [4, 5, 5, 2, 1]  
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 4, key = 3, j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[1] = 4, j = -1 할당.  
        j >= 0 아니므로 while loop 종료.  
        a = [4, 4, 5, 2, 1]  
      - ##### for loop 하단, while loop 종료 후 x[j + 1] = key  
      x[0] = 3 값이 할당  
      a = [3, 4, 5, 2, 1]  

    - #### for loop i = 3 값을 가질 때, j = i - 1, key = x[i]    
    j = 2, key = x[3] (value 2 할당)  
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 5, key = 2, j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[3] = 5, j = 1 할당됨.  
        j >= 0 이므로 while loop 지속.  
        a = [3, 4, 5, 5, 1]
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 4, key = 2, j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[2] = 4, j = 0 할당.  
        j >= 0 이므로 while loop 지속.  
        a = [3, 4, 4, 5, 1]
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 3, key = 2, j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[1] = 3, j = -1 할당.  
        j >= 0 아니므로 while loop 종료.  
        a = [3, 3, 4, 5, 1]
      - ##### for loop 하단, while loop 종료 후 x[j + 1] = key  
      x[0] = 2 값이 할당  
      a = [2, 3, 4, 5, 1]  

    - #### for loop i = 4 값을 가질 때, j = i - 1, key = x[i]    
    j = 3, key = x[4] (value 1 할당)  
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 5, key = 1, j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[4] = 5, j = 2 할당됨.  
        j >= 0 이므로 while loop 지속.  
        a = [2, 3, 4, 5, 5]
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 4, key = 1, j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[3] = 4, j = 1 할당.  
        j >= 0 이므로 while loop 지속.  
        a = [2, 3, 4, 4, 5]
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 3, key = 1, j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[2] = 3, j = 0 할당.  
        j >= 0 이므로 while loop 지속.  
        a = [2, 3, 3, 4, 5]
      - ##### while loop x[j] > key and j >= 0:  
      x[j] = 2, key = 1, j >= 0 이므로 while 문 작동  
        - ##### while loop x[j + 1] = x[j], j = j - 1  
        x[1] = 2, j = -1 할당.  
        j >= 0 아니므로 while loop 종료.  
        a = [2, 2, 3, 4, 5]
      - ##### for loop 하단, while loop 종료 후 x[j + 1] = key  
      x[0] = 1 값이 할당  
      a = [1, 2, 3, 4, 5]  



- jupyter notebook  

```python
a = [5, 4, 3, 2, 1]

def insertion_sort(x):
    for i in range(1, len(x)):
        j = i - 1
        key = x[i]
        print(f'i: {i}\n-----while 시작-----')
        while x[j] > key and j >= 0:
            print('값 변경 전', a)
            x[j + 1] = x[j]
            print('크기비교 후 값 변경', a)
            j = j - 1
            print('-----while 끝-----')
        x[j + 1] = key
        print('for, while 문 끝난 후 값 변경', a)
    return x

insertion_sort(a)
```
```1
i: 1
-----while 시작-----
값 변경 전 [5, 4, 3, 2, 1]
크기비교 후 값 변경 [5, 5, 3, 2, 1]
-----while 끝-----
for, while 문 끝난 후 값 변경 [4, 5, 3, 2, 1]
i: 2
-----while 시작-----
값 변경 전 [4, 5, 3, 2, 1]
크기비교 후 값 변경 [4, 5, 5, 2, 1]
-----while 끝-----
값 변경 전 [4, 5, 5, 2, 1]
크기비교 후 값 변경 [4, 4, 5, 2, 1]
-----while 끝-----
for, while 문 끝난 후 값 변경 [3, 4, 5, 2, 1]
i: 3
-----while 시작-----
값 변경 전 [3, 4, 5, 2, 1]
크기비교 후 값 변경 [3, 4, 5, 5, 1]
-----while 끝-----
값 변경 전 [3, 4, 5, 5, 1]
크기비교 후 값 변경 [3, 4, 4, 5, 1]
-----while 끝-----
값 변경 전 [3, 4, 4, 5, 1]
크기비교 후 값 변경 [3, 3, 4, 5, 1]
-----while 끝-----
for, while 문 끝난 후 값 변경 [2, 3, 4, 5, 1]
i: 4
-----while 시작-----
값 변경 전 [2, 3, 4, 5, 1]
크기비교 후 값 변경 [2, 3, 4, 5, 5]
-----while 끝-----
값 변경 전 [2, 3, 4, 5, 5]
크기비교 후 값 변경 [2, 3, 4, 4, 5]
-----while 끝-----
값 변경 전 [2, 3, 4, 4, 5]
크기비교 후 값 변경 [2, 3, 3, 4, 5]
-----while 끝-----
값 변경 전 [2, 3, 3, 4, 5]
크기비교 후 값 변경 [2, 2, 3, 4, 5]
-----while 끝-----
for, while 문 끝난 후 값 변경 [1, 2, 3, 4, 5]
```
