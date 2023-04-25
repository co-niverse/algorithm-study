#2445
num = int(input())
for i in range(1,2*num):
  if i <= num:
    print("*"*i+" "*(2*num-2*i)+"*"*i)
  else:
    print("*"*(2*num-i)+" "*(2*(i-num))+"*"*(2*num-i))


#2522
num = int(input())
for i in range(1,num+1):
    print(" "*(num-i)+"*"*i)
for j in range(1,num):
    print(" "*j + "*"*(num-j))


#2446
num = int(input())
for i in range(num):
    print(" "*i+"*"*(2*num-1-2*i))
for j in range(2,num+1):
    print(" "*(num-j)+"*"*(2*j-1))


#10991
num = int(input())
for i in range(1,num+1):
    print(" "*(num-i) + "* "*i)


#10992
num = int(input())
if(num!=1):
    print(" "*(num-1)+"*")
for i in range(1,num-1):
    print(" "*(num-i-1)+"*" + " "*(2*(i)-1)+"*")
print("*"*(2*num-1))
