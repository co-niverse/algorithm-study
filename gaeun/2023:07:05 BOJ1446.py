n ,d = map(int,input().split())
shortcuts = []
distances = [0]*(d+1)
for _ in range(n):
    shortcuts.append(list(map(int,input().split())))

for i in range(1,d+1):
    distances[i]= distances[i-1]+1
    for s in shortcuts :
        if s[1] == i :
            distances[i] = min(distances[i],distances[s[0]]+s[2])

print(distances[d])

    