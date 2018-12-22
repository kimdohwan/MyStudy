import sys
from random import randrange, shuffle, seed

seed(2)
class Maze:
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.vis = [[0] * self.w + [1] for _ in range(self.h)] + [[1] * (self.w + 1)]
        self.hor = [["##"] * self.w + ['#'] for _ in range(self.h + 1)]
        self.ver = [["# "] * self.w + ['#'] for _ in range(self.h)] + [[]]

        self.maze = self._make_maze()

    # 미로를 생성 return type = str
    def _make_maze(self):

        start_x, start_y = randrange(self.w), randrange(self.h)
        self._create_map(start_x, start_y)

        maze = ''
        for (h, v) in zip(self.hor, self.ver):
            maze += ''.join(h + ['\n'] + v + ['\n'])
        return maze

    # _make_maze() 에서 사용되는 재귀함수
    def _create_map(self, x, y):
        self.vis[y][x] = 1

        direction = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        shuffle(direction)
        for (xx, yy) in direction:
            if self.vis[yy][xx]:
                continue
            if xx == x:
                self.hor[max(y, yy)][x] = '# '
            if yy == y:
                self.ver[y][max(x, xx)] = '  '

            self._create_map(xx, yy)

    def solve(self):
        convert_maze = self.maze.split('\n')
        (sx, sy), (ex, ey) = self.get_start_end_point(convert_maze)

        self._find_path(convert_maze, sx, sy, ex, ey)

    def _find_path(self, convert_maze, sx, sy, ex, ey):
        visited = self.copy_multidimensional_list(
            li=convert_maze,
            data=False,
            target='#',
            target_data=None,
        )

        distance = self.copy_multidimensional_list(
            li=convert_maze,
            data=(self.w * 2 - 1) * self.h,
            target='#',
            # target_data=sys.maxsize,
            target_data=99,
        )
        distance[sy][sx] = 0

        prev = self.copy_multidimensional_list(
            li=convert_maze,
            data=None,
            target='#',
            target_data=[-1, -1],
        )
        prev[sy][sx] = 1

        x, y = sx, sy
        px, py = sx, sy
        direction = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        stack = [] + direction

        while True:
            if (x, y) == (ex, ey):
                break
            if visited[y][x] is not None and distance[y][x] > distance[py][px] + 1:
                direction = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
                stack += direction

                visited[y][x] = True
                distance[y][x] = distance[py][px] + 1
                prev[y][x] = [px, py]
                px, py = x, y
                self.change_maze(convert_maze, x, y, '.')

            now = stack.pop()
            x, y = now[0], now[1]

        px, py = prev[ey][ex]
        # while True:
        #     prev[py][px] = x, y
        #     self.change_maze(convert_maze, x, y, '.')

    def change_maze(self, maze, x, y, to_string):
        maze[y] = maze[y][:x] + to_string + maze[y][x + 1:]
        print('y,x', maze[y][x], x, y)
        for i in maze: print(i)

    def copy_multidimensional_list(self, **kwargs):
        multidimensional_list = []
        for i in range(len(kwargs['li'])):
            multidimensional_list.append([])
            for j in range(len(kwargs['li'][i])):
                if kwargs['li'][i][j] == kwargs.get('target'):
                    multidimensional_list[i].append(kwargs['target_data'])
                else:
                    multidimensional_list[i].append(kwargs['data'])
        return multidimensional_list

    # 출발 ,도착 지점의 index(좌표) 를 계산.(리스트로부터)
    def get_start_end_point(self, convert_maze):
        for y in range(len(convert_maze)):
            for x, s in enumerate(convert_maze[y]):
                if s == 'S':
                    sx, sy = x, y
                elif s == 'E':
                    ex, ey = x, y
        return (sx, sy), (ex, ey)

    # 출발, 도착 지점을 self.maze 에 만듭니다. random_point=True 라면 랜덤으로 지점 생성합니다.
    def set_start_end(self, random_point=False):
        if random_point:
            while True:
                start_point = randrange(len(self.maze))
                end_point = randrange(len(self.maze))
                if start_point != end_point and ' ' in self.maze[start_point] and ' ' in self.maze[end_point]:
                    break
        else:
            for i, s in enumerate(self.maze):
                if s == ' ':
                    start_point = i
                    break
            for i, s in enumerate(reversed(self.maze)):
                if s == ' ':
                    end_point = len(self.maze) - i - 1
                    break

        self.maze = self.maze[:start_point] + 'S' + self.maze[start_point + 1:]
        self.maze = self.maze[:end_point] + 'E' + self.maze[end_point + 1:]

    # 문자열을 변경해주는 함수. 코드 간결화하기 위해 사용

    def __repr__(self):
        return f'Maze({self.w}, {self.h})'

    def __str__(self):
        return self.maze


if __name__ == '__main__':
    m1 = Maze(10, 5)
    print(repr(m1))

    m1.set_start_end(
        # random_point=True
    )
    print(m1)

    m1.solve()
