bar = input()
sum = 0
stack = []

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append('(')

    else:
        if bar[i-1] == '(': 
            stack.pop()
            sum += len(stack)

        else:
            stack.pop() 
            sum += 1 

print(sum)
