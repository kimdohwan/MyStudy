import random
import copy
import numpy

def quick_sort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        quick_sort(a, low, pivot -1)
        quick_sort(a, pivot + 1, high)

def partition(a, pivot, high):
    current_a = a[pivot: high + 1]
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j


if __name__ == '__main__':
    a = numpy.random.choice(10, 6, replace=False)
    print(a)
    quick_sort(a, 0, len(a) - 1)
    print(a)