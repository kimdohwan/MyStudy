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
def set_start_end(maze):
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
    return maze, (start_x, start_y), (end_x, end_y)


# 2차원 배열을 크기만큼 복사하고 item 을 넣어준 후 start 지점은 0으로 셋팅
def make_distance_list(maze, min_val, sx, sy):
    distance = []
    for i in range(len(maze)):
        distance.append([])
        for j in range(len(maze[i])):
            distance[i].append(min_val)
    distance[sy][sx] = 0

    return distance


def copy_mutiple_list(li, item):
    result = []
    for i in range(len(li)):
        result.append([])
        for j in range(len(li[i])):
            result[i].append(item)
    return result


def solve(w, h):
    min_value = 100

    make = make_maze(w, h)
    convert = convert_maze(make)
    maze, (sx, sy), (ex, ey) = set_start_end(convert)
    # sx, sy = pos_start[0], pos_start[1]
    # ex, ey = pos_end[0], pos_end[1]

    # change_str(maze, 3, 4, ' ')

    for i in maze: print(i)

    visited = maze[:]
    prev = copy_mutiple_list(maze, [0, 0])
    distance = make_distance_list(maze, min_value, sx, sy)

    def find_path(x, y):
        # if visited[y][x] in [' ', 'S']:
        if x == ex and y == ey:
            return True
        elif visited[y][x] == ' ':
            change_str(visited, y, x, '?')
            d = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
            for xx, yy in d:
                if visited[yy][xx] != '#' and distance[yy][xx] > distance[y][x] + 1:
                    distance[yy][xx] = distance[y][x] + 1
                    prev[yy][xx] = [x, y]
                if find_path(xx, yy):
                    change_str(maze, yy, xx, '.')
                    return True
        # elif visited[y][x] == 'E':
        return False

    find_path(sx, sy)

    print('maze')
    for i in maze: print(i)
    print('distance')
    for i in distance: print(i)
    print('visited')
    for i in visited: print(i)
    print('prev')
    for i in prev: print(i)

    # visited T/F list - cache maze
    # distance comparison list - ?
    # result list - prev_list


if __name__ == '__main__':
    solve(4, 2)
