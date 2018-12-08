import sys

N = 8
s = 0
g = [None for i in range(N)]
g[0] = [(1, 1), (3, 2)]
g[1] = [(0, 1), (2, 4), (3, 3), (4, 1), (5, 6)]
g[2] = [(1, 4), (5, 1), (6, 1), (7, 2)]
g[3] = [(0, 2), (1, 3), (4, 5)]
g[4] = [(1, 1), (3, 5), (6, 2)]
g[5] = [(1, 6), (2, 1), (7, 9)]
g[6] = [(2, 1), (4, 2), (7, 1)]
g[7] = [(2, 2), (5, 9), (6, 1)]

visited = [False for i in range(N)]
D = [sys.maxsize for i in range(N)]
D[s] = 0
previous = [None for i in range(N)]
previous[s] = s

# 코드 구조는 prim algorithm 과 거의 듀사하다
# 다른부분은 최소거리값을 갱신하는 부분인데
# 누적된 값을 구해서 거리를 비교하는 방식으로 동작한다.
# 또한 prim 의 경우 visited=True 라는 의미가
# 하나의 트리구조로 편입됫음을 의미해서 트리의 전체 edges 의 weight 를
# 고려하는 방식이다. 이 때 visited=Ture 인 vertex 는 더이상
# 최소비용 계산을 하지 않아도되는 고정된 값이지만
# dijkstra 의 경우 visited=True 에 관계없이
# 최소거리 값이 변할 수 있다는 점이 다르다.
for k in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j

    visited[m] = True

    for w, wt in g[m]:

        # if not visited[w] 라는 구문은 없다 왜?
        # 특정 vertex 까지의 최소 거리를 구하는 알고리즘에서는
        # 최소 거리를 얻는 거이 목적이기 때문에
        # 이미 방문/트리 의 유무에 관계없이 vertex 를 이용할 수 있다.
        # 따라서 이미 최소거리값(D[w])이 셋팅되어있고 visited=True더라도
        # 새로운 weight 로 갱신가능하다.
        if D[m] + wt < D[w]:
            D[w] = D[m] + wt
            previous[w] = m

print(f'정점 {s} 로부터의 최단거리: ')
for i in range(N):
    if D[i] == sys.maxsize:
        print(f'{s} 와 {i} 사이에 경로 없음')
    else:
        print(f'({s}, {i}) = {D[i]} ')

print(f'정점 {s} 로부터의 최단경로: ')
for i in range(N):
    back = i
    print(back, end='')
    while back != s:
        print(f' <- {previous[back]}', end='')
        back = previous[back]
    print()

if __name__ == '__main__':
    pass
