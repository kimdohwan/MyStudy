from random import shuffle, randrange, seed

__all__ = (
    'make_maze',
)


# 미로 생성하는 함수
def make_maze(w, h):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["# "] * w + ['#'] for _ in range(h)] + [[]]
    hor = [["##"] * w + ['#'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "# "
            if yy == y:
                ver[y][max(x, xx)] = "  "
            walk(xx, yy)

    seed(2)
    walk(randrange(w), randrange(h))

    result = []
    for (a, b) in zip(hor, ver):
        result.append(''.join(a + ['\n'] + b))
    return result


if __name__ == '__main__':
    for i in make_maze(16, 4):
        print(i)
