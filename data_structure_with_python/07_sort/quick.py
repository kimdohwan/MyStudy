import random
import copy
import numpy


def quick_sort(a, low, high):

    # call stack 의 가장 위에서 stack 을 제자리로 돌리는 역할,
    # if 문에 걸리지 않는다?
    # 앞뒤로 쪼개지다가 더이상 정렬이 필요없는 경우를 의미,
    if low < high:

        # pivot 값을 구할 때 정렬 실행한다
        # 입력된 list a 를 pivot(현재 함수의 low값)을 기준으로
        # 왼쪽에는 pivot 보다 작은 값, 오른쪽에는 pivot 보다 큰 값으로
        # 정렬 후 반환되는 값이 pivot 값으로 설정된다.
        # 여기서 pivot 값은 partition() 에 의해 자기 자리에 정렬 된 값이다.
        # 따라서 pivot 을 제외한 나머지 item 들의 정렬이 필요하다.
        # pivot 을 기준으로 앞, 뒤가 나뉘게 되고 재귀적으로 앞, 뒤 정렬을 실행해준다.
        pivot = partition(a, low, high)
        quick_sort(a, low, pivot - 1)
        quick_sort(a, pivot + 1, high)


def partition(a, pivot, high):
    current_a = a[pivot: high + 1]  # debug 때 정렬 범위 보려고 만든 변수

    i = pivot + 1  # 새로운 low 값에 해당한다. pivot 보다 작은 값이 할당되어야 한다.
    j = high  # 정렬하려는 list 의 마지막 값으로, pivot 보다 큰 값이 할당되어야 한다.
    while True:

        # i 는 해당리스트의 마지막 값 high 를 초과할 수 없다.
        # 초과한다면 out of range Exception 날 것이다.
        # 아니다. 뒷부분을 정렬 시킨다면 out of range 이겠지만
        # 앞부분을 정렬할 경우, 이미 정렬 완료 된 pivot 값을 건드리게 된다.
        # 그러면 안되지!
        while i < high and a[i] < a[pivot]:
            # pivot 보다 작으면 +1 로 다음 값 검사하다가
            # pivot 보다 큰 수 만나면 i 를 보관!(교환해야지!)
            i += 1
        while j > pivot and a[j] > a[pivot]:
            # a[pivot] < a[j] 라면 ok, -1 로 다음 값 검사하다가
            # pivot 보다 작은 수 만나면 j값 보관(교환해야지!)
            j -= 1

        # i 와 j 가 만났다는 것은
        # list 의 모든 값(검사하기로 한 index 범위내의) 비교를 실행 했음을 의미,
        # 이 구문은 i, j 값 교환을 종료시키고 pivot 값 설정으로 넘어가기위해 존재
        if i >= j:
            break

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    # 왜 j 인가? pivot 과 교체되는 값은 무조건 pivot 보다 작아야 한다.
    # while loop 를 마친 후 j 값은 pivot 값보다 작게되고,
    # i 값은 pivot 값보다 크게된다.
    # 지금 작성한 코드의 경우,
    # pivot 이 list[0] 으로 설정되어있으므로
    # 정렬이 끝난 뒤 pivot 이 교환되어야 하는 자리(위치해야하는)는
    # pivot 값보다 작은 값인 j 가 되는 것이다.
    # 하지만 반대로 pivot 값을 list 의 가장 마지막 값으로 설정한다면
    # pivot 의 위치인 list[end] 에는
    # pivot 보다 큰수가 와야한다.(이 경우 i 와 값교환 성립)
    a[pivot], a[j] = a[j], a[pivot]

    # 여기서 return 하는 j 의 의미,
    # a[j] 는 정렬된 값(자기 자리를 찾았음)이다.
    # j 의 왼쪽에는 j 보다 작은 숫자가 위치하고 오른쪽에는 j보다 큰 수가 위치한다.
    # j 에는 pivot 값이 위치하게 된다.
    return j


if __name__ == '__main__':
    a = numpy.random.choice(10, 10, replace=False)
    print(a)
    quick_sort(a, 0, len(a) - 1)
    print(list(a))
