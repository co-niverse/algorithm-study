import sys
from collections import deque
readline = sys.stdin.readline
l,c = map(int,readline().split())
alphabets = list(map(str,readline().split()))
alphabets.sort()
result = []

def makePW(first):
    vowel = False
    consonant = 0
    if alphabets[first] in ["a","e","i","o","u"] :
        vowel = True
    if not alphabets[first] in ["a","e","i","o","u"] :
        consonant +=1

    queue = deque([[alphabets[first],first,vowel,consonant]])
    while queue :
        info = queue.popleft()
        pw = info[0]
        index = info[1]
        vowel = info[2]
        consonant = info[3]
        if len(pw) < l :
            for ind in range(index+1,c) :
                nextVowel = vowel
                nextConsonant = consonant
                if nextVowel == False and alphabets[ind] in ["a","e","i","o","u"] :
                    nextVowel = True
                if not alphabets[ind] in ["a","e","i","o","u"] :
                    nextConsonant +=1
                queue.append([pw+alphabets[ind],ind,nextVowel,nextConsonant])
        else :
            if vowel and consonant >= 2 :
                result.append(pw)





for i in range(len(alphabets)) :
    makePW(i)

for pw in result :
    print(pw)

