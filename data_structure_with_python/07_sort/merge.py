#!/usr/bin/env python
import random


def merge_sort(a, b, low, high):
    # debug mode 에서 list item 확인을 위해 추가한 변수
    current_list = a[low: high + 1]

    # 보통 logN 의 복잡도를 가지는 정렬의 경우,
    # list 를 앞, 뒤 2개로 쪼개가며 call stack 의 가장 윗단에서는
    # list item 이 1개만 남을 때까지 2개로 쪼개는 함수가 실행된다.
    # 쪼개고 쪼개다 보면 결국 item 이 1개가 될 때가 온다
    # 함수의 list item 이 1개라는 의미는,
    # caller(stack 의 한단계 밑 함수)함수의 list item 은 2개라는 것을 뜻한다.
    # 보통 2개로 쪼개는 정렬 함수의 경우,
    # 2개의 재귀 함수(앞, 뒤를 담당하는)가 실행되는데
    # 이 때 앞, 뒤를 담당하는 함수 모두 list item 이 1개 되면 return 을 한다.
    # 앞,뒤 함수가 모두 return 된 상태에서 크기비교 연산(값 변경, 할당)을 실행한다.
    # 2개, 2개로 나뉘어진 list item 들이 각각 정렬된 후에,
    # 총 4개의 list item 을 재배치(정렬)하게 된다
    # quick sort 의 경우,
    # 크기비교 연산(값 변경, 할당)에서 이뤄지는 과정이 약간 다르지만
    # 2개로 쪼개지며 재귀적으로 함수를 호출하는 방식은 매우 유사하다.
    if high <= low:
        return f'{current_list}'  # return 만 적는 것이 맞음(debug 때 보려고 문자열 추가)
    mid = low + (high - low) // 2

    # 처음에는 2개의 list item 을 가지고 들어간다.
    # 실행 된 후에는 a[0], a[1] 이 정렬 완료
    merge_sort(a, b, low, mid)

    # 처음에는 2개의 list item 을 가지고 들어간다.
    # 실행 된 후에는 a[2], a[3] 이 정렬 완료
    merge_sort(a, b, mid + 1, high)

    # 위 두 함수가 실행된 후 2개씩 쪼개져 정렬된(a[0], a[1] / a[2], a[3])
    # 총 4개이 list item 을 정렬시킨다
    merge(a, b, low, mid, high)


def merge(a, b, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high + 1):

        # 2개/2개로 쪼개진 item 들의 첫번째 item 크기 비교?
        # 아니다. item 이 아닌 index 크기비교다. 왜?
        # 알아냈다
        # for loop 가 실행됫을 때(k=0)부터 최소 절반까지(mid 값)까지는
        # 3,4 번째 if 문'만' 실행된다.
        # 왜냐하면 그 전까지는 i, j 가 mid, high 값을 초과할 수 없기 때문이다.
        # i, j 가 mid,high 를 초과한다는 의미는
        # 반으로 쪼갠 각각의 list index 를 넘어섰다는 것인데
        # 이 때 넘어선 값은 mid or high 값이 되겠다.
        # i 값이 mid 를 초과했다면, i 부터 mid 까지의 값들은 list b 에 할당되어있다(정렬 완료되었다)
        # j 값이 hight 를 초과했다면 j 부터 high 까지의 값들은 list b 에 할당되어있다(정렬 완료되었다)
        # 그러므로 아직 할당되지 않은(mid or high를 초과하지 않은) 값을
        # list b 에 할당(정렬)하고 index 를 증가시켜(+1) 다음 값 할당을 진행한다.
        if i > mid:
            b[k] = a[j]
            j += 1
        elif j > high:
            b[k] = a[i]
            i += 1

        # list item 값들을 비교한다.
        # i, j +1 하는 이유:
        #   b 에 a[x] 를 넣게 된다면, x 에 해당하는 값은 정렬이 완료됫음을 의미
        #   따라서 그 다음 값을 정렬연산해주어야 한다. +1 해줘서 index 를 바꿔준다
        #   else 의 경우는 같은 값을 비교할 경우도 포함된다(ex: a[i] == a[j])
        elif a[j] < a[i]:
            b[k] = a[j]
            j += 1
        else:
            b[k] = a[i]
            i += 1

    # # ---------------------- 내가 바꿔본 코드(속도 더 느림ㅠㅠ)-------------
    #     k = low
    #     while i <= mid and j <= high:
    #         if a[i] > a[j]:
    #             b[k] = a[j]
    #             j += 1
    #         else:
    #             b[k] = a[i]
    #             i += 1
    #         k += 1
    #
    #     while i < mid + 1 or j < high + 1:
    #         if i > mid:
    #             b[k] = a[j]
    #             j += 1
    #         elif j > high:
    #             b[k] = a[i]
    #             i += 1
    #         k += 1
    #
    # # -------------------------------------------------------------

    # 정렬된 list b 의 item 을 a로 복사해준다.
    for k in range(low, high + 1):
        a[k] = b[k]


if __name__ == '__main__':
    a = [random.randint(0, 50) for i in range(10)]
    # a = [39, 6, 33, 18]
    b = [None] * len(a)
    print(a)
    merge_sort(a, b, 0, len(a) - 1)
    print(a)
    print(b)
