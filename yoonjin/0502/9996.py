n = int(input())
pattern = input().split("*")

for i in range(n):
    str = input()
    if len(pattern[0]) + len(pattern[1]) > len(str):
        print("NE")
    else:
        if(pattern[0] == str[:len(pattern[0])] and pattern[1] == str[-len(pattern[1]):]):
            print("DA")
        else:
            print("NE")
