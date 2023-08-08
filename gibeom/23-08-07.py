from sys import stdin

s, t = stdin.readline().rstrip(), list(stdin.readline().rstrip())
while len(s) != len(t):
    last = t.pop()
    if last == "B":
        t = t[::-1]

print(1) if s == "".join(t) else print(0)

##########################
#    memory: 31256KB     #
#    time:   40ms        #
##########################
