from sys import stdin


def check_button(limit, next):
    move_cnt = res
    channel = 100
    while channel != limit:
        for num in str(channel):
            if num in broken:
                break
        else:
            move_cnt = min(move_cnt, len(str(channel)) + abs(channel - n))
        channel += next
    return move_cnt


n, m = int(stdin.readline()), int(stdin.readline())
broken = set(stdin.readline().split())

res = abs(n - 100)
if n == 100:
    print(0)
elif m == 0:
    print(min(res, len(str(n))))
elif m == 10:
    print(res)
else:
    if 100 < n:
        print(min(res, check_button(1000001, 1)))
    else:
        print(min(res, check_button(-1, -1)))

##########################
#    memory: 31256KB     #
#    time:   464ms       #
##########################
