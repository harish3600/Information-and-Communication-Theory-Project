# Question 2
#(a) n = 15, k = 10, p = 0.015

#Part 1 - Create Random Code
import random

def BSC(codeword,p):
    newcode = []
    n = len(codeword)
    for i in range(n):
        cur = random.random();
        if(cur<p):
            if(codeword[i]==0):
                newcode[i]=1
            elif(codeword[i]==1):
                newcode[i]=0
    return newcode


n = 5
k = 2
p = 0.015
code = []

codeC = []
cnt = 0
while(cnt<(2**k)):
#    print("Codeword No.: ",i)
    codeword = []
    for length in range(n):
        codeword.append(random.randint(0,1))
    if codeword not in codeC:
        codeC.append(codeword)
        cnt += 1

#    print(codeword)

N = 100
c = [[0,1,3,4,5],[0,1,2,4,5]]

print(codeC)
