from random import randrange, shuffle


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
        # self._create_map(start_x, start_y, vis=vis, ver=ver, hor=hor)
        self._create_map(start_x, start_y)

        maze = ''
        for (h, v) in zip(self.hor, self.ver):
            maze += ''.join(h + ['\n'] + v + ['\n'])
        return maze

    # _make_maze() 에서 사용되는 재귀함수
    def _create_map(self, x, y):
        # kwargs['vis'][y][x] = 1
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

    def set_start_end(self):
        randrange(len())
        pass

    def solve(self):
        pass

    def __repr__(self):
        return f'Maze({self.w}, {self.h})'

    def __str__(self):
        return self.maze


if __name__ == '__main__':
    m1 = Maze(12, 6)
    print(repr(m1))
    print(m1)
    # print(m1.solve())
