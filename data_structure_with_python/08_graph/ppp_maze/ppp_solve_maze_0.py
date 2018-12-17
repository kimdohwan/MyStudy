from ppp_make_maze import make_maze


def change_str(string, y, x, s):
    string[y] = string[y][:x] + s + string[y][x + 1:]


def solve(w, h):
    # 주어진 w, h 로 w x h 크기의 미로를 생성
    maze = make_maze(w, h)

    # \n 을 기준으로 maze list 를 새로 만들어준다.
    convert_maze = []
    for i in maze:
        for j in i.split('\n'):
            convert_maze.append(j)

    # 왼쪽,위 귀퉁이를 start 지점으로 만듭니다.
    y = 0
    while y < len(convert_maze):
        x = 0
        z = x
        while x < len(convert_maze[y]):
            z += 1
            if convert_maze[y][x] == ' ':
                sx = x
                sy = y
                change_str(convert_maze, y, x, 'S')
                break
            x += 1
        if x != z:
            break
        y += 1

    # 오른,아래 귀퉁이를 end 지점으로 만듭니다.
    # 주석 처리 한 부분은 E pos 를 왼쪽 아래 귀퉁이로 만드는 코드
    y = len(convert_maze) - 1
    while y >= 0:
        x = len(convert_maze[y]) - 1
        # x = 0
        z = x
        while x >= 0:
        # while x < len(convert_maze[y]):
            z -= 1
            # z += 1
            if convert_maze[y][x] == ' ':
                ex = x
                ey = y
                change_str(convert_maze, y, x, 'E')
                break
            x -= 1
            # x += 1
        if x != z:
            break
        y -= 1

    # find_path() 에서 maze visited 를 기록 할 복사본 cache list
    maze_cache = convert_maze[:]

    # 경로 탐색 함수
    def find_path(x, y):
        # 걸러지는 경우: 상하좌우가 모두 #, ' ', ? 인 경우
        # 실행되는 경우: 상하좌우에 ' ' 가 존재 하는 경우(방문하지 않은 곳이 존재)
        if maze_cache[y][x] in [' ', 'S']:
            change_str(maze_cache, y, x, '?')
            # ? 를 입력하고, ? 의 상하좌우 지점이 True 라면 . 입력
            # . 입력하는 경우는 아직 가보지 않은 지점에서 상하좌우에 아직 가보지 않은 지점이 있는 경우
            if find_path(x + 1, y) or find_path(x - 1, y) or find_path(x, y + 1) or find_path(x, y - 1):
                change_str(maze_cache, y, x, '.')
                change_str(convert_maze, y, x, '.')
                return True

        elif maze_cache[y][x] == 'E':
            return True
        return False

    find_path(sx, sy)

    print('convert maze')
    for i in convert_maze:
        print(i)

    print('maze cache')
    for i in maze_cache:
        print(i)

    return convert_maze


if __name__ == '__main__':
    solve(24, 12)
