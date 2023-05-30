n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
mArray = list(map(int, input().split()))

def binary_search(array, target, start, end):
  while (start <= end):
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
  return None

for target in mArray:
    result = binary_search(array,target,0,n-1)
    if result == None:
        print(0)
    else:
        print(1)
