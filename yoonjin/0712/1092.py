import sys
input = sys.stdin.readline

n = int(input())
crane_weight = list(map(int, input().split())) #6 8 9
crane_list = [0] * n # 0 0 0

m = int(input())
box = list(map(int, input().split())) # 2 5 2 4 7
check_box = [0] * m

# box, crane_weight를 무거운 순서대로 내림차순 정렬
box.sort(reverse=True) # 7 5 4 2 2
crane_weight.sort(reverse=True) # 9 8 6

error = 0
for i in range(m):
    least = []
    for j in range(n): # 7
      if box[i] <= crane_weight[j]:
        least.append(j) # 0 1
      if box[i] > max(crane_weight):
        error = 1
    if (len(least) == 0):
        minL = 1e9
        minLin = 1e9
        for l in range(n):
          if minL > crane_list[l]:
            minL = crane_list[l]
            minLin = l
        crane_list[minLin] += 1
        #check_box[i] = 1
    else:
        # least에 있는 것들 중 crane_list 값이 제일 적은 곳에 +1
        minK = 1e9
        minKin = 1e9
        for k in range(len(least)): 
          if minK > crane_list[least[k]]:
            minK = crane_list[least[k]]
            minKin = k
        crane_list[least[minKin]] += 1
        #check_box[i] = 1

if error:
  print(-1)
else:
  print(max(crane_list))
