from sys import stdin

n, m = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
room = [stdin.readline().split() for _ in range(n)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
clean_cnt = 1
while True:
    room[r][c] = "2"

    for _ in range(4):
        d = (d + 3) % 4
        nr, nc = r + direction[d][0], c + direction[d][1]
        if room[nr][nc] == "0":
            r, c = nr, nc
            clean_cnt += 1
            break
    else:
        r, c = r - direction[d][0], c - direction[d][1]
        if room[r][c] == "1":
            break

print(clean_cnt)

##########################
#    memory: 31256KB     #
#    time:   44ms        #
##########################
