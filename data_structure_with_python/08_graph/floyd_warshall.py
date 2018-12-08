import sys

N = 5
INF = sys.maxsize
D = [[0, 4, 2, 5, INF],
     [INF, 0, 1, INF, 4],
     [1, 3, 0, 1, 2],
     [-2, INF, INF, 0, 2],
     [INF, -3, 3, 1, 0]]

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])


for i in range(N):
    for j in range(N):
        print(f'{D[i][j]:3d}  ', end='')
    print()

if __name__ == '__main__':
    pass
