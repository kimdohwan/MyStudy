import random


def radix_sort(a, base=10):
    size = len(a)
    maxval = max(a)
    exp = 1

    while exp <= maxval:
        output = [0] * size
        count = [0] * base

        for i in range(size):
            count[(a[i] // exp) % base] += 1

        for i in range(1, base):
            count[i] += count[i - 1]

        for i in range(size - 1, -1, -1):
            j = (a[i] // exp) % base
            output[count[j] - 1] = a[i]
            count[j] -= 1

        for i in range(size):
            a[i] = output[i]

        exp *= base


if __name__ == '__main__':
    a = random.sample(range(0, 100), 4)
    print(a)
    radix_sort(a)
    print(a)