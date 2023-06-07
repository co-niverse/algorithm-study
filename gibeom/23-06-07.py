from sys import stdin


def is_out_of_range(r, c, r_end, c_end, start):
    return r < start or r > r_end or c < start or c > c_end


def move(r, c, d, r_end, c_end, start):
    if is_out_of_range(r + direction[d][0], c + direction[d][1], r_end, c_end, start):
        d = (d + 1) % 4
    return r + direction[d][0], c + direction[d][1], d


N, M, R = map(int, stdin.readline().split())
arr = [list(stdin.readline().split()) for _ in range(N)]
res = [[None] * M for _ in range(N)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(min(N, M) // 2):
    r_len, c_len = N - 1 - i * 2, M - 1 - i * 2

    element_cnt = (r_len + c_len) * 2
    turn_cnt = R % element_cnt

    r, c = i, i
    if turn_cnt < element_cnt // 2:
        if turn_cnt < r_len:
            r += turn_cnt
            d = 0
        else:
            r += r_len
            c += turn_cnt - r_len
            d = 1
    else:
        turn_cnt -= element_cnt // 2
        if turn_cnt < r_len:
            r += r_len - turn_cnt
            c += c_len
            d = 2
        else:
            c += c_len - (turn_cnt - r_len)
            d = 3

    nr, nc, nd = i, i, 0
    while element_cnt:
        res[r][c] = arr[nr][nc]
        r, c, d = move(r, c, d, i + r_len, i + c_len, i)
        nr, nc, nd = move(nr, nc, nd, i + r_len, i + c_len, i)

        element_cnt -= 1

for re in res:
    print(*re)

##########################
#    memory: 37168KB     #
#    time:   196ms       #
##########################
