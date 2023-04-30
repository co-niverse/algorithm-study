n = int(input())

for i in range(n):
    stack = []
    vps = input()
    for i in vps:
      if i == "(":
        stack.append("(")
      elif i == ")":
        if len(stack)!=0 and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(")")
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
