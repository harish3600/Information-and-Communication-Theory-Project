# Question 2
#(a) n = 15, k = 10, p = 0.015

#Part 1 - Create Random Code
import random

def BSC(codeword,p):
    n = len(codeword)
    newcode = [0]*n
    for i in range(n):
        cur = random.random();
        if(cur<p):
            if(codeword[i]==0):
                newcode[i]=1
            elif(codeword[i]==1):
                newcode[i]=0
        else:
            newcode[i] = codeword[i]
    return newcode


n = 10
k = 2

codeC = []
cnt = 0

#Creating Random Code with 2^k codewords
while(cnt<(2**k)): 
#    print("Codeword No.: ",i)
    codeword = []
    for length in range(n):
        codeword.append(random.randint(0,1))
    if codeword not in codeC:
        codeC.append(codeword)
        cnt += 1
#    print(codeword)


N = 5
p = 0.1

E = 0

#print(codeC)
for i in range(N):
    cur = random.randint(0,(2**k)-1)
    c = codeC[cur]
    y = BSC(c,p) #Recieved Codeword from BSC - y
    mindiff = n+1;
    estInd = 0

    #Minimum Distance Decoding Algorithm
    for t in range(2**k): #Iterating through all codewords in C to compare which codeword has minimum hamming distance with y(Received Codeword)
        diff = 0
        for ind in range(n):
            if(y[ind]!=codeC[t][ind]):
                diff += 1;
        if diff<mindiff: #If current difference obtained is lesser than stored difference,
            estInd = t  # store the index of the new difference
            mindiff = diff #  we update the minimum difference
    cEst = codeC[estInd]
    if(cEst!=c): #If the estimated codeword does not match the input codeword, we increment error
        E += 1 # E - Number of errors in decoding by the decoding algorithm
    print("I ",i)
    print("P ",c)
    print("R ",y)
    print("E ",cEst)
    print('\n')

print(E)
