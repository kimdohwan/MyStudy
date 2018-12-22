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
        pass

    def change_maze(self, arr, x, y, to_string):
        arr[y] = arr[y][x:] + to_string + arr[y][x + 1:]
        pass

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

    def __repr__(self):
        return f'Maze({self.w}, {self.h})'

    def __str__(self):
        return self.maze


if __name__ == '__main__':
    m1 = Maze(12, 6)
    print(repr(m1))
    print(m1)

    m1.set_start_end(
        # random_point=True
    )

    print(m1.maze)
