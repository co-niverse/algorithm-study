# import sys
# read = sys.stdin.readline
# T = int(read().strip())

# def findShort(W,K):
#     result = []
#     for w in range(len(W)) :
#         kCount = 0
#         replica = W
#         value = ""
#         # 자신과 동일한 문자 K개 이상 찾기
#         for target in range(w+1,len(W)) :
#             if W[w]==W[target] :
#                 kCount +=1
#                 if kCount == K-1 :
#                     value = W[w:target+1]
#                     break
#         # K개 이상 있을 때
#         if value != "":
#             replica=replica.replace(value,len(value))
#             result.append(replica)
#     return result

# def findLong(ind,W):
#     for w in range(ind-1,-1,-1) :
#         # 자신과 동일한 문자 찾기
#         for target in W[ind+1:] :
#             if W[w]==W[target] :
#                 return target-w
#     return -1

                

# for t in range(T) :
#     W = str(read().strip())
#     K = int(read().strip())
#     short = findShort(W,K)
#     resultList = []
#     for string in short :
#         ind = -1
#         for s in range(len(string)) :
#             if not string[s].isalpha() :
#                 ind = s
#                 break
#         num = findLong(ind,string)
#         if num != -1 :
#             resultList.append((ind,num))
#     if len(resultList) == 0 :
#         print(-1)
#     else:
#         resultList.sort(reverse=True)
#         print(resultList[0])


import sys
from collections import defaultdict
read = sys.stdin.readline
T = int(read().strip())
for t in range(T) :
    W = str(read().strip())
    K = int(read().strip())

    dict = defaultdict(list)
    for ind,w in enumerate(W):
        if W.count(w) >= K :
            dict[w].append(ind)
    
    short = 1e9
    long = -1
    for w, itemList in dict.items() :
        if len(itemList)==K :
            first = itemList[0]
            last = itemList[len(itemList)-1]
            stringSize = last-first+1
            if stringSize < short :
                short = stringSize
            if stringSize > long :
                long = stringSize
        elif len(itemList) >=K :
            for i in range(len(itemList)-K+1):
                first = itemList[i]
                last = itemList[i+K-1]
                stringSize = last-first+1
                if stringSize < short :
                    short = stringSize
                if stringSize > long :
                    long = stringSize
    if short == 1e9 or long ==-1:
        print(-1)
    else :
        print(short,long)


