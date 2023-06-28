from sys import stdin


def dfs(res, idx):
    global max_res, min_res

    if idx == n:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:
                dfs(res + nums[idx], idx + 1)
            elif i == 1:
                dfs(res - nums[idx], idx + 1)
            elif i == 2:
                dfs(res * nums[idx], idx + 1)
            else:
                dfs(int(res / nums[idx]), idx + 1)
            operators[i] += 1


n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
operators = list(map(int, stdin.readline().split()))

max_res = int(-1e9)
min_res = int(1e9)
dfs(nums[0], 1)

print(max_res)
print(min_res)

##########################
#    memory: 31256KB     #
#    time:   76ms        #
##########################
