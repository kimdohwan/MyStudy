#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # 조건 1: k 가 s와 t 삭제, 추가를 넉넉히 커버하는 경우
    if len(s) + len(t) < k:
        return 'Yes'

    # 공통 str 구하기
    count = 0
    while count < min(len(s), len(t)):
        if s[count] == t[count]:
            count += 1
        else:
            break

    # 조건 2: s + t 에서 공통 문자열을 제외한 개수가 k 보다 크면 No
    result = len(s) + len(t) - 2 * count
    if result > k:
        return 'No'

    # 조건 3:
    # - y, yu, 2 의 경우
    # 1. y 를 지우면(+1) y, u 추가(+2)에서 실패(3 != 2)
    # 2. u를 추가(+1)하면 실패(1 != 2)
    # 맞는 결과: No
    # 해결 방법:
    #   공통된 문자(y)를 제외한 문자(u)의 홀짝 여부가 다르게되면
    #   k 의 크기가 문자 추가를 할 수 있는 값이 충분히 큼에도
    #   1 차이로 실패할 수밖에 없게된다.

    #   사례를 들어 k 에 1, 2, 3, 4 인 경우를 각각 따져보자
    #   k = 1, Yes(2번 결과와 매칭)
    #   k = 2, No(문제 답))
    #   k = 3, Yes(1번 결과과 매칭)
    #   k = 4, Yes(조건 1에서 3보다 큰 수는 모두 Yes 로 걸러짐)
    #   따라서 k = 2 인 경우, No 처리하는 조건 필요
    #        k = 1, 3 인 경우, Yes 처리하는 조건 필요

    #   조건 1을 통과 한 후 남는 수들(1, 2, 3)의 경우 홀/짝여부 일치에 따라서
    #   Yes, No 를 판별해야 한다는 것을 알 수 있다.

    # s + t 에서 공통 문자열을 제외한 문자의 개수 홀/짝 여부가
    # k 의 홀/짝 여부와 같은 경우
    result = result % 2
    if result == k % 2:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
