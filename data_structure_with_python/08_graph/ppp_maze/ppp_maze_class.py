from random import randrange, shuffle


class Maze:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.maze = self._make_maze()

    # 미로를 생성 return type = str
    def _make_maze(self):
        vis = [[0] * self.w + [1] for _ in range(self.h)] + [[1] * (self.w + 1)]
        hor = [["##"] * self.w + ['#'] for _ in range(self.h + 1)]
        ver = [["# "] * self.w + ['#'] for _ in range(self.h)] + [[]]

        start_x, start_y = randrange(self.w), randrange(self.h)
        self._create_map(start_x, start_y, vis=vis, ver=ver, hor=hor)

        maze = ''
        for (h, v) in zip(hor, ver):
            maze += ''.join(h + ['\n'] + v + ['\n'])
        return maze

    # _make_maze() 에서 사용되는 재귀함수
    def _create_map(self, x, y, **kwargs):
        kwargs['vis'][y][x] = 1

        direction = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        shuffle(direction)
        for (xx, yy) in direction:
            if kwargs['vis'][yy][xx]:
                continue
            if xx == x:
                kwargs['hor'][max(y, yy)][x] = '# '
            if yy == y:
                kwargs['ver'][y][max(x, xx)] = '  '

            self._create_map(xx, yy, **kwargs)

    def __repr__(self):
        return f'Maze({self.w}, {self.h})'

    def __str__(self):
        return self.maze


if __name__ == '__main__':
    m1 = Maze(12, 6)
    print(repr(m1))
    print(m1)
