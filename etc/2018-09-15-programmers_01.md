
#### 문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

- 제한사항
s는 길이가 1 이상, 100이하인 스트링입니다.

- 입출력 예

  | s | return |
  |:-----:|:-----:|
  | "abcde" | "c" |
  | "qwer" | "we" |

#### 문제 풀이 1(내 코드)
```1
def solution(s):
    len_by_two = len(s) // 2
    if 0 != len(s) % 2:
        answer = s[len_by_two]
    else:
        answer = s[len_by_two - 1: len_by_two + 1]
    return answer
```

#### 문제 풀이 2(좋아요 1등)
```1
def string_middle(str):
    return str[(len(str) - 1) // 2: len(str) // 2 + 1]
```

#### 생각해보기
- 짝수 문자열의 경우 return 해야 하는 문자가 2개여야 하므로 slicing 과정이 꼭 필요하지만 홀수의 경우엔 문자가 1개뿐이므로 단순하게 해당 index 만 return 하였다.  
하지만 1개의 문자만 return 하는 경우에도 [4: 5] 와 같은 방식이 가능할 수 있다.  
좋아요 1등 코드의 경우, list slicing 을 통해 홀수와 짝수의 경우를 if 를 사용하지 않고 나머지 연산에 -1, +1 연산을 통해 해결해주었다.  
- 한줄 정리 : list slicing 으로 두가지 경우(홀, 짝)를 if 사용 없이 한줄로 구현
- 필요한 능력
  - list slicing 응용하는 능력: 파이썬 언어에 대한 이해
  - 나머지 연산(소수점 자르기)에 대한 이해: 수학적 논리력? 혹은 직접 삽집해보며 값을 확인해볼수도..  
