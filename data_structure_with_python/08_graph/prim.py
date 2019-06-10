import sys

N = 7
s = 0  # 처음 선택되는 임의의 vertex, start
g = [None] * N  # 각 vertex 가 가진 edge 들을 list 로 가진다

g[0] = [(1, 9), (2, 10)]
g[1] = [(0, 9), (3, 10), (4, 5), (6, 3)]
g[2] = [(0, 10), (3, 9), (4, 7), (5, 2)]
g[3] = [(1, 10), (2, 9), (5, 4), (6, 8)]
g[4] = [(1, 5), (2, 7), (6, 1)]
g[5] = [(2, 2), (3, 4), (6, 6)]
g[6] = [(1, 3), (3, 8), (4, 1), (5, 6)]

visited = [False] * N  # 트리에 포함되었는지 여부를 나타냄, 순회/방문 했냐의 여부
D = [sys.maxsize] * N  # weight 를 기록하며 갱신할 리스트

# 시작점 s 의 weight? 간선은 결국 N-1개 이므로 weight 또한 N-1 개가된다.
# (0이되는 값 1개 존재-> 출발점)
D[s] = 0
previous = [None] * N  # 연결되는 vertex 을 기록하는 리스트

# 시작점 s, 자기 자신을 가르킨다. 의미없음(시작점을 의미하니까)
# 주석처리해도 없어도 되는 코드다.
# 시작하자마자 previous[0] 은 True 가 되게되서 list previous[0] 에
# 값을 할당하는 구문자체가 실행이 될 수 없어서이다. 하지만 이해를 돕기위해 책 그대로 적자
previous[s] = s

# loop 를 N 만큼 수행, 매 loop 마다 vertex 를 하나씩 트리화/방문 한다
for k in range(N):
    m = -1  # 왜있는 부분이지? 의미적으로도 코드적으로도 영향이 없는듯
    min_value = sys.maxsize  # list D 의 간선 연산을 편하게 하기위한 수단 maxsize

    # '연결 가능한' edges(간선들) 중 weight(가중치)가 가장 작은 항목을 고릅니다.
    # 여기서 '연결 가능한'은 list D 에 갱신된 값이 존재함을 의미합니다.
    # 또한 list previous 에는 list D 의 weight 값의 edge 가 연결되는 vertex(정점)을 가집니다
    # N 번의 loop 를 돌며 (각각의 vertex 의 트리화/방문 여부 + 가중치가 가장 작은 edge 검색)
    for j in range(N):

        # m 을 정함: 트리에 포함될 정점/방문,순회 할 정점
        # min_value 변수를 통해 최소값을 가진 vertex 찾아냅니다.
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j

    # True 로 트리화/방문을 하게되면,
    # 연결시킬 wt 최소값 검색 연산(위 for loop)과
    # 연결시킬 간선 갱신 연산(아래 for loop)에서
    # visited True 에 의해 제외된다.
    # 왜냐? 이미 같은 집합이므로, 이미 연결되어있으니까 연결대상으로 고려할 필요가 없다.
    # 하지만 그 뒤에 연결되는 vertex 에 의해 간선연결 생길수는 있다.
    visited[m] = True

    # 연결시킬 간선의 최소값을 갱신하는 for loop
    # 위에 True 로 새 트리를 완성시켰으므로 트리에 연결되는 간선과 가중치를 다시 갱신해야함.
    # 새로 편입된 정점 m 이 가진 간선들 중에서
    # 가중치 비교를 통해 더 작은 가중치로 갱신(D), 연결시킬 정점 후보(previous) 갱신.
    for w, wt in list(g[m]):
        if not visited[w]:
            if wt < D[w]:
                D[w] = wt  # 1번의 가중치를 더 작은 값으로 바꿔준다
                previous[w] = m  # 그리고 1번이 연결되는 지점을 6번으로 reset 해준다

if __name__ == '__main__':
    print('최소신장트리: ', end='')
    mst_cost = 0
    for i in range(1, N):
        print(f'({i}, {previous[i]})', end='')
        mst_cost += D[i]
    print(f'\n weights of minimum spanning tree: {mst_cost}')
