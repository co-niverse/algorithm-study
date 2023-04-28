from collections import deque
import sys
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
s1 = set(A)
s2 = set(B)
sum = 0
sum+=len(s1-s2)
sum+=len(s2-s1)
print(sum)
