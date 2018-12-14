from random import shuffle

from ppp_make_maze import make_maze


def solve(w, h):
    maze = make_maze(w, h)
    maze[0] = maze[0][:35] + 'S' + maze[0][36:]
    maze[3] = maze[3][:65] + 'E' + maze[3][66:]

    m = []
    for i in maze:
        for j in i.split('\n'):
            m.append(j)

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'S':
                start_x = j
                start_y = i
            if m[i][j] == 'E':
                end_x = j
                end_y = i

    # def s(x, y):
    #     m[y] = m[y][:x] + '.' + m[y][x + 1:]
    #     d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
    #     shuffle(d)
    #     for (xx, yy) in d:
    #         print(xx, yy)
    #
    #         if m[yy][xx] in ['.', '#']:
    #             continue
    #
    #         if xx == x:
    #             m[max(y, yy)] = m[max(y, yy)][:x] + "." + m[max(y, yy)][x + 1:]
    #         if yy == y:
    #             m[y] = m[y][:max(x, xx)] + "." + m[y][max(x, xx) + 1:]
    #         s(xx, yy)
    def s(x, y):
        if m[y][x] in [' ', 'S']:
            m[y] = m[y][:x] + '?' + m[y][x + 1:]

            if s(x + 1, y) or s(x - 1, y) or s(x, y + 1) or s(x, y - 1):
                m[y] = m[y][:x] + '.' + m[y][x + 1:]

                return True
        elif m[y][x] == 'E':
            return True
        return False

    s(start_x, start_y)

    # n = 0
    # while n < 9999:
    #     if m[end_y][end_x] == m[start_y][start_x]:
    #         break
    #     if m[start_y][start_x] in ['?', '#']:
    #         continue
    #
    #     if m[start_y + 1][start_x] == ' ':
    #         m[start_y + 1] = \
    #             m[start_y + 1][:start_x] + '?' + m[start_y + 1][start_x + 1:]
    #     if m[start_y][start_x + 1] == ' ':
    #         m[start_y] = \
    #             m[start_y][:start_x + 1] + '?' + m[start_y][start_x + 1 + 1:]
    #     if m[start_y - 1][start_x] == ' ':
    #         m[start_y - 1] \
    #             = m[start_y - 1][:start_x] + '?' + m[start_y - 1][start_x + 1:]
    #     if m[start_y][start_x - 1] == ' ':
    #         m[start_y] \
    #             = m[start_y][:start_x - 1] + '?' + m[start_y][start_x - 1 + 1:]
    #
    #     n += 1
    #     for i in m:
    #         print(i)
    for i in m:
        print(i)
    for i in maze:
        print(i)


if __name__ == '__main__':
    solve(16, 4)
