adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1],
            [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
N = len(adj_list)
visited = [False for x in range(N + 1)]

result = []  # 디버그를 위해 추가한 list


def breath_first_search(i):
    queue = []
    visited[i] = True  # 방문여부를 기록?
    queue.append(i)
    while len(queue) != 0:  # queue 에 append 된 항목들에는 방문을 했다는 기록은 있지만 정점을 방문한 순서는 기록되어있지 않다. 순서라는 부분을 해결하기위해 queue 자료구조를 이용하여 먼저 방문한 정점을 먼저 기록하여 순서를 매기는 것이 가능해진다. 여기서 pop 은 FIFO 의 순서에 해당하는 의미도 있지만 queue 에 들어가있는 정점이 없게된다면 더 이상 방문한 정점이 없다는 것을 의미하게되어 함수가 종료되고 bfs 함수 밖에 있는 for loop 에 의해 연결없이 따로 떨어져서 구성 된 정점항목(i)를 새로 함수의 인자로 받게된다.
        v = queue.pop(0)  # visited 를 True 로 설정한 항목을 queue 에서 pop(0), 그냥 pop() 을 해주게 되면 스택 구조처럼 마지막 값이 pop 된다 명심하자
        print(v, ' ', end='')  # pop 된 정점은 방문을 마쳤다.
        result.append(v)  # debug 를 위해 추가한 코드
        for w in adj_list[v]:  # pop 된 정점에 adjacency list 를 방문하기위한 for loop
            if not visited[w]:  # 인접한 정점 w 가 아직 방문이 없었다면
                visited[w] = True  # 방문을 한 후
                queue.append(w)  # queue 에 추가한다. 왜? pop 으로 방문순서를 정해주려고. queue 는 순차적으로 방문한 노드의 순서를 append 로 기록해 놓는다. 일단 인접한 정점들을 기록하고 정점의 정점을 순차적으로 방문한다. 그리고 pop 을 통해 순회 순서를 알 수 있다. dfs 와는 다르게 순회 시 정점의 정점만을 따라가는 방법이 아니라 인접한 정점을 모두 방문하고 정점의 정점들을 또다시 모두 방문해야하므로 queue list 로 방문의 기록을 남겨야할 필요가 있다. 이 차이점을 잘 기억하고 응용하자.


print('breath first search: ')
for i in range(N):
    if not visited[i]:
        breath_first_search(i)

if __name__ == '__main__':
    pass
