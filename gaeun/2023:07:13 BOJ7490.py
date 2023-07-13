import sys
readline = sys.stdin.readline
#방법1
def calculateNum(n,ind,calculate):
    if ind == n-1 :
        value = 1
        withCount = 0
        if not "-" in calculate:
            return
        for i in range(n-1):
            if calculate[i] == "+":
                if withCount > 0 :
                    cal = calculate[i-1-withCount]
                    if cal == "+" :
                        value-= i+1-withCount
                        value +=int(''.join(map(str, numList[i-withCount:i+1])))
                    elif cal == "-" :
                        value += i+1-withCount
                        value -=int(''.join(map(str, numList[i-withCount:i+1])))
                    withCount = 0
                    value+= i+2
                else:
                    value+= i+2
            elif calculate[i] == "-":
                if withCount > 0 :
                    cal = calculate[i-1-withCount]
                    if cal == "+" :
                        value-= i+1-withCount
                        value +=int(''.join(map(str, numList[i-withCount:i+1])))
                    elif cal == "-" :
                        value += i+1-withCount
                        value -=int(''.join(map(str, numList[i-withCount:i+1])))
                    
                    withCount = 0
                    value-= i+2
                else :
                    value-= i+2
            elif calculate[i] == " ":
                withCount+=1
                if i == n-2:
                    cal = calculate[i-withCount]
                    if cal == "+" :
                        value-= i+2-withCount
                        value +=int(''.join(map(str, numList[i+1-withCount:i+2])))
                    elif cal == "-" :
                        value += i+2-withCount
                        value -=int(''.join(map(str, numList[i+1-withCount:i+2])))

        if value == 0 :
            string = ""
            for i in range(n):
                string+=str(numList[i])
                if i <= n-2 :
                    string+=calculate[i]
            print(string)
        return
    elif ind > n-1 :
        return
    else :
        calculate.append(" ")
        calculateNum(n,ind+1,calculate)
        calculate.pop()
        calculate.append("+")
        calculateNum(n,ind+1,calculate)
        calculate.pop()
        calculate.append("-")
        calculateNum(n,ind+1,calculate)
        calculate.pop()
        

t = int(readline())
tList = []
n=-1
for _ in range(t):
    m = int(readline())
    tList.append(m)
for m in tList:
    n=m 
    numList = [i for i in range(1,n+1)]
    resultList = []

    calculateNum(n,1,[" "])
    calculateNum(n,1,["+"])
    calculateNum(n,1,["-"])
    print("\n")
    
#방법2

def calculateNum(n,ind,calculate):
    if ind == n-1 :
        calculationList.append(list(calculate))
        return 
    else :
        calculate.append(' ')
        calculateNum(n,ind+1,calculate)
        calculate.pop()
        calculate.append("+")
        calculateNum(n,ind+1,calculate)
        calculate.pop()
        calculate.append("-")
        calculateNum(n,ind+1,calculate)
        calculate.pop()
        

t = int(readline())
for _ in range(t):
    n = int(readline())
    calculationList = []
    numList = [i for i in range(1,n+1)]
    calculateNum(n,1,[' '])
    calculateNum(n,1,["+"])
    calculateNum(n,1,["-"])
    for cal in calculationList :
        string = ""
        for i in range(n-1):
            string+=str(numList[i])
            string+=cal[i]
        string+=str(numList[-1])
        
        if eval(string.replace(' ','')) == 0 :
            print(string)
    print()