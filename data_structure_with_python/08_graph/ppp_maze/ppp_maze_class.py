from random import randrange, shuffle


class Maze:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.maze = self.make_maze()

    def make_maze(self):
        vis = [[0] * self.w + [1] for _ in range(self.h)] + [[1] * (self.w + 1)]
        ver = [["# "] * self.w + ['#'] for _ in range(self.h)] + [[]]
        hor = [["##"] * self.w + ['#'] for _ in range(self.h + 1)]

        start_x, start_y = randrange(self.w), randrange(self.h)

        self.create_map(start_x, start_y, vis=vis, ver=ver, hor=hor)

        maze = ''
        for (a, b) in zip(hor, ver):
            maze.join(a + '\n' + b + '\n')

        return maze

    def create_map(self, x, y, **kwargs):
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

            self.create_map(xx, yy, **kwargs)

    def __repr__(self):
        return f'{self.make()}'

    # def __str__(self):
    #     return f'{self.make()}'


if __name__ == '__main__':
    m = Maze(12, 6)
