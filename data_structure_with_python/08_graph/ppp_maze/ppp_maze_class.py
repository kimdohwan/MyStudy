import sys
from random import randrange, shuffle, seed


class Maze:
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.vis = [[0] * self.w + [1] for _ in range(self.h)] + [[1] * (self.w + 1)]
        self.hor = [["##"] * self.w + ['#'] for _ in range(self.h + 1)]
        self.ver = [["# "] * self.w + ['#'] for _ in range(self.h)] + [[]]

        self.convert_maze = None
        self.distance = None
        self.prev = None
        self.visited = None

        self.maze = self._maze

    # 미로의 노드(길 1칸을 의미) 갯수. node size - 1 은 edge 의 최댓값이 된다.
    @property
    def node_size(self):
        n = 0
        for i in self._maze:
            for j in i:
                if j in [' ']:
                    n += 1
        return n

    @node_size.setter
    def node_size(self, value):
        node_size = value

    # @node_size.getter
    # def node_size(self):
    #     return 'getter'

    # 미로를 생성 return type = str
    @property
    def _maze(self):

        start_x, start_y = randrange(self.w), randrange(self.h)
        self._create_map(start_x, start_y)

        maze = ''
        for (h, v) in zip(self.hor, self.ver):
            maze += ''.join(h + ['\n'] + v + ['\n'])
        return maze

    # _maze() 에서 사용되는 재귀함수
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
        self.set_start_end_point()
        self.convert_maze = self.maze.split('\n')
        (sx, sy), (ex, ey) = self._get_start_end_point()

        self.visited = self._copy_multidimensional_list(
            li=self.convert_maze,
            data=False,
            target='#',
            target_data=None,
        )

        self.distance = self._copy_multidimensional_list(
            li=self.convert_maze,
            data=self.node_size,
            target='#',
            # target_data=sys.maxsize,
            target_data=999,
        )
        self.distance[sy][sx] = 0

        self.prev = self._copy_multidimensional_list(
            li=self.convert_maze,
            data=None,
            target='#',
            target_data=[-1, -1],
        )
        self.prev[sy][sx] = 1

        self._find_path(sx, sy)
        self._get_minimum_path(sx, sy, ex, ey)

        solve_maze = ''
        for i in self.convert_maze:
            solve_maze += ''.join(i + '\n')

        return solve_maze

    def _find_path(self, x, y):
        direction = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        for xx, yy in direction:
            if self.visited[yy][xx] is not None and self.distance[yy][xx] > self.distance[y][x] + 1:
                self.distance[yy][xx] = self.distance[y][x] + 1
                self.prev[yy][xx] = [x, y]
                self._find_path(xx, yy)

        if self.visited[y][x] is False:
            self.visited[y][x] = True

    def _get_minimum_path(self, sx, sy, ex, ey):
        x, y = self.prev[ey][ex]
        while True:
            self._change_string(self.convert_maze, x, y, '.')
            x, y = self.prev[y][x]
            if (x, y) == (sx, sy):
                break

    # 문자열을 변경해주는 함수. 코드 간결화하기 위해 사용
    @staticmethod
    def _change_string(string, x, y, to_string):
        string[y] = string[y][:x] + to_string + string[y][x + 1:]

    @staticmethod
    def _copy_multidimensional_list(**kwargs):
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
    def _get_start_end_point(self):
        (sx, sy), (ex, ey) = (None, None), (None, None)
        for y in range(len(self.convert_maze)):
            for x, s in enumerate(self.convert_maze[y]):
                if s == 'S':
                    sx, sy = x, y
                elif s == 'E':
                    ex, ey = x, y
        return (sx, sy), (ex, ey)

    # 출발, 도착 지점을 self._maze 에 만듭니다. random_point=True 라면 랜덤으로 지점 생성합니다.
    def set_start_end_point(self, random_point=False):
        start_point, end_point = None, None
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

    def __repr__(self):
        return f'Maze({self.w}, {self.h})'

    def __str__(self):
        return self.maze


if __name__ == '__main__':
    seed()
    m1 = Maze(6, 3)
    print(repr(m1))
    print(m1)

    # print(m1.solve())
    print(m1.node_size)
    m1.node_size = 1
    print(m1.node_size)
    # print(m1._node_size)
