import sys
from random import shuffle, seed, randint, randrange

from ppp_make_maze import make_maze


# index 와 str 을 입력받아 문자열을 변경
def change_str(string, y, x, s):
    string[y] = string[y][:x] + s + string[y][x + 1:]


# \n split 실행(list 로 return)
def convert_maze(maze):
    c_maze = []
    for i in maze:
        for j in i.split('\n'):
            c_maze.append(j)
    return c_maze


# maze 의 start, end 를 생성
# 두번째 인자가 존재 할 경우 랜덤으로 지점 생성
def set_start_end(maze, rd=False):
    if rd:
        seed(rd)
        while True:
            start_y = randrange(len(maze) - 1)
            start_x = randrange(len(maze[0]))
            end_y = randrange(len(maze) - 1)
            end_x = randrange(len(maze[0]))
            if maze[start_y][start_x] == ' ' \
                    and maze[end_y][end_x] == ' ' \
                    and (start_x, start_y) != (end_x, end_y):
                break

    else:
        y = 0
        start_x, start_y = None, None
        while y < len(maze):
            x = 0
            z = x
            while x < len(maze[y]):
                z += 1
                if maze[y][x] == ' ':
                    start_x = x
                    start_y = y
                    # change_str(maze, y, x, 'S')
                    break
                x += 1
            if x != z:
                break
            y += 1

        y = len(maze) - 1
        while y >= 0:
            x = len(maze[y]) - 1
            z = x
            while x >= 0:
                z -= 1
                if maze[y][x] == ' ':
                    end_x = x
                    end_y = y
                    # change_str(maze, y, x, 'E')
                    break
                x -= 1
            if x != z:
                break
            y -= 1
    return (start_x, start_y), (end_x, end_y)


# 2차원 배열을 크기만큼 복사하고 item 을 넣어준 후 start 지점은 0으로 셋팅
def make_distance_list(maze, min_val, sx, sy):
    distance = []
    for i in range(len(maze)):
        distance.append([])
        for j in range(len(maze[i])):
            distance[i].append(min_val)
    distance[sy][sx] = 0

    return distance


# 2차원 배열을 복사하고 item 을 넣어줍니다.
def copy_mutiple_list(li, item):
    result = []
    for i in range(len(li)):
        result.append([])
        for j in range(len(li[i])):
            result[i].append(item)
    return result


# 경로 탐색과 벽 없애기 반복 시 랜덤 생성할지 정합니다.
def create_random_seed(random_seed):
    if random_seed:
        seed()
        if type(random_seed) == int:
            seed_number = random_seed
            seed(seed_number)
            return seed_number
        seed_number = randrange(sys.maxsize)
        seed(seed_number)
        return seed_number
    return random_seed


# 벽을 없앨지 말지 정하며, 시드 지정이 가능합니다.
def remove_wall(maze, random_remove):
    if random_remove:
        seed(random_remove)
        n = 0
        while n < 5:
            ry = randrange(1, len(maze) - 1 - 1)
            rx = randrange(1, len(maze[0]) - 1)
            if maze[ry][rx] == '#':
                change_str(maze, ry, rx, ' ')
                n += 1


# 미로 실험을 위해서 랜덤으로 미로, 시작지점, 벽제거를 위한 기능을 추가했다
# 기능 = random on/off + seed 지정
def solve(w, h, random_maze=False, random_point=False, random_remove=False, print_element=True):
    maze_seed_number = create_random_seed(random_maze)
    point_seed_number = create_random_seed(random_point)
    remove_wall_seed_number = create_random_seed(random_remove)

    # 거리(가중치)비교를 위한 최대값 생성 - 미로의 전체 넓이만큼 셋팅.
    # 왜냐하면 가장 거리가 큰 지점은 path(노드)의 갯수 -1 이기 때문이다
    # 벽이 포함되었기때문에 2로 나누어줬다. 넉넉한 숫자이다.
    min_value = (((w * 2) + 1) * ((h * 2) + 1)) // 2

    # 미로를 생성하고 적합한 형태로 바꿔준다(convert)
    create_maze = make_maze(w, h, maze_seed_number)
    maze = convert_maze(create_maze)

    remove_wall(maze, remove_wall_seed_number)

    # 시작, 끝 지점을 생성한다
    (sx, sy), (ex, ey) = set_start_end(maze, point_seed_number)

    # visited: 미로가 방문한 곳을 체크해준다
    visited = maze[:]
    # prev: 미로의 최소 경로를 기록한다(이전 노드 기록, for loop 로 출력해야한다)
    # prev 의 기본값은 [0, 0](아무 값이나 넣어도 관계없다. 출력했을 때 보기 쉬운 형태로 넣자)
    # start 지점에는 'START' 라는 문자열을 넣어준다(경로가 존재하지 않으므로)
    prev = copy_mutiple_list(maze, [0, 0])
    prev[sy][sx] = ['START']
    # distance: start 지점(0 할당)을 제외한 모든 지점에 min_value 할당
    distance = make_distance_list(maze, min_value, sx, sy)

    # 1. <방문한 지점(visited)> 체크
    # 2. <이동 방향(상하좌우)> for loop 실행
    #   2-1. <이동 가능(!=벽) / 최소 경로 갱신 가능> if 검사
    #       2-1-1. <거리 / 이전 노드> 갱신
    #       2-1-2. 이동한 지점에서 <경로 탐색> 을 재귀 -> 중요한 지점
    #   2-2. start, end point 를 보기쉽게하기 위한 용도(중요X, 없애도 됨)
    def find_path(x, y):
        if visited[y][x] == ' ':
            change_str(visited, y, x, 'V')
        left_right_up_down = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        # shuffle(left_right_up_down)  # 모든 지점을 방문할 것이기 때문에 필요없는 옵션
        for xx, yy in left_right_up_down:
            if visited[yy][xx] != '#' and distance[yy][xx] > distance[y][x] + 1:
                distance[yy][xx] = distance[y][x] + 1
                prev[yy][xx] = [x, y]
                find_path(xx, yy)
            if (xx, yy) in [(sx, sy), (ex, ey)]:
                change_str(visited, yy, xx, ' ')
                if (xx, yy) == (sx, sy):
                    change_str(maze, yy, xx, 'S')
                else:
                    change_str(maze, yy, xx, 'E')

    # prev 노드 추적으로 최적경로 표시
    def assgin_prev_to_maze():
        n = 0
        x = ex
        y = ey
        while True:
            n += 1
            x, y = prev[y][x][0], prev[y][x][1]
            if (x, y) == (sx, sy):
                break
            change_str(maze, y, x, '.')

        # 프린트하기 귀찮으니 예외발생 시켜서 검사하자
        if n != distance[ey][ex]:
            raise Exception(n != distance[ey][ex])

    def make_maze_to_string():
        string_maze = ''
        for i in maze:
            string_maze += i + '\n'

        return string_maze

    # 경로찾기 시작
    find_path(sx, sy)
    assgin_prev_to_maze()
    result = make_maze_to_string()

    if print_element:
        print('distance')
        for i in distance: print(i)
        print('visited')
        n = 0
        for i in range(len(visited)):
            for j in visited[i]:
                if j == ' ':
                    n += 1
            print(visited[i])
        if n != 2:
            raise Exception(n != 2, '모든 노드를 방문하지 않았습니다')
        print('prev')
        for i in prev: print(i)
        print('maze')
        for i in maze: print(i)

    return print(result)


if __name__ == '__main__':
    solve(
        3,
        2,
        random_maze=True,
        random_point=False,
        random_remove=False,
        print_element=False,
    )
