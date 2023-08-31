#최종 방법
import sys
readline = sys.stdin.readline
n, m = map(int, readline().split())
setList = [i for i in range(n+1)]

def findRoot(ind) :
    # 만약 자신의 노드가 다른 루트 자식이라면
    if setList[ind] != ind :
        #자신이 바라보고 있는 루트의 루트를 찾음
        setList[ind] = findRoot(setList[ind]) 
    return setList[ind]

#실제로 합치는 것이 아닌, 트리구조로 루트,자식으로 관계를 표현
def union(x,y):
    #각자가 바라보고 있는 최상위 root
    rootX = findRoot(x)
    rootY = findRoot(y)
    # rootY도 rootX와 같은 루트를 바라보고 있음으로써 , 같은 집합에 포함
    setList[rootY] = rootX



for _ in range(m):
    calcul,a,b = map(int,readline().split())
    #합집합
    if calcul == 0 :
        union(a,b)
    #조회
    else :
        if findRoot(a)==findRoot(b):
            print("yes")
        else :
            print("no")










# 방법 1 메모리초과
# import sys
# readline = sys.stdin.readline
# n, m = map(int, readline().split())
# setList = [set([i]) for i in range(n + 1)]


# for j in range(m):
#     calcul , a , b = map(int,readline().split())
#     aSet = 0
#     bSet = 0
#     if calcul == 0 :
#         if a !=b :
#             for idx, setValue in enumerate(setList):
#                 if a in setValue :
#                     aSet = idx              
#                 elif b in setValue:
#                     bSet = idx
#             newSet = setList[aSet].union(setList[bSet])
#             setList[aSet] = newSet
#             setList.remove(setList[bse])
#     else :
#         flag = False
#         for setValue in setList :
#             if a in setValue and b in setValue:
#                 print("yes")
#                 flag = True
#                 break
#         if flag == False :
#             print("no")
            

#방법1 메모리누수 확인
# import sys
# import psutil

# readline = sys.stdin.readline

# def get_memory_usage():
#     return psutil.Process().memory_info().rss / 1024 / 1024  # in MB
# n, m = map(int, readline().split())

# initial_memory = get_memory_usage()
# setList = [set([i]) for i in range(n + 1)]


# for j in range(m):
#     calcul , a , b = map(int,readline().split())
#     aSet = 0
#     bSet = 0
#     if calcul == 0 :
#         if a !=b :
#             for idx, setValue in enumerate(setList):
#                 if a in setValue :
#                     aSet = idx              
#                 elif b in setValue:
#                     bSet = idx
#             current_memory = get_memory_usage()
#             print("current_memory : " ,current_memory)
#             if current_memory > 128:  # Threshold in MB
#                 print(f"Memory usage exceeded 128MB at iteration {j}, current usage: {current_memory:.2f} MB")

#             newSet = setList[aSet].union(setList[bSet])
#             current_memory = get_memory_usage()
#             print("current_memory : " ,current_memory)
#             if current_memory > 128:  # Threshold in MB
#                 print(f"Memory usage exceeded 128MB at iteration {j}, current usage: {current_memory:.2f} MB")
#             setList[aSet] = newSet
#             setList.remove(setList[bSet])
#     else :
#         flag = False
#         for setValue in setList :
#             if a in setValue and b in setValue:
#                 print("yes")
#                 flag = True
#                 break
#         if flag == False :
#             print("no")



















# 방법2
# import sys
# readline = sys.stdin.readline
# n, m = map(int, readline().split())

# setList = [i for i in range(n+1)]  # 각 정점을 단일 집합으로 초기화

# def find_set(x):
#     if setList[x] != x:
#         setList[x] = find_set(setList[x])  # 경로 압축
#     return setList[x]

# def union_sets(x, y):
#     root_x = find_set(x)
#     root_y = find_set(y)
#     if root_x != root_y:
#         setList[root_y] = root_x

# for _ in range(m):
#     calcul, a, b = map(str, readline().split())
#     a = int(a)
#     b = int(b)
    
#     if calcul == '0':
#         union_sets(a, b)
#     else:
#         if find_set(a) == find_set(b): # 부모의 루트 노드가 같은지 확인
#             print("yes")
#         else:
#             print("no")




#방법3 메모리 초과 set을 union하는 과정에서 메모리 초과 발생
# import sys
# readline = sys.stdin.readline
# n,m = map(int,readline().split())
# setList = [set(str(i)) for i in range(n+1)]

# for j in range(m):
#     calcul , a , b = map(str,readline().split())
#     aSet = set()
#     bSet = set()
#     if calcul == '0' :
#         if a !=b :
#             for setValue in setList :
#                 if a in setValue :
#                     aSet = setValue              
#                 elif b in setValue:
#                     bSet = setValue
#             newSet = set.union(aSet,bSet)
#             setList.remove(aSet)
#             setList.remove(bSet)
#             setList.append(newSet)
#     else :
#         flag = False
#         for setValue in setList :
#             if a in setValue and b in setValue:
#                 print("yes")
#                 flag = True
#                 break
#         if flag == False :
#             print("no")
            

