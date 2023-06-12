num = list(map(str,input()))
minValue = []
maxValue = []
mcount = 0
for ind,i in enumerate(num) :
    if i == 'M':
        mcount +=1
        if ind == len(num)-1 :
            maxValue.append('1'*mcount)
            minValue.append(str(10**(mcount-1))) 
    else :
        if mcount == 0 :
          maxValue.append('5')
          minValue.append('5')
        else :
            maxValue.append(str((10**mcount)*5))
            minValue.append(str(10**(mcount-1)))
            minValue.append('5')
            mcount = 0
print(''.join(map(str,maxValue)))
print(''.join(map(str,minValue)))
