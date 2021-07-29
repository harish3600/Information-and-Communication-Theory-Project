# Question 2
#(a) n = 15, k = 10, p = 0.015

#Part 1 - Create Random Code
import random
n = 5
k = 2
p = 0.015
code = []

for i in range(2**k):
    print("Codeword No.: ",i)
    codeword = []
    for length in range(n):
        codeword.append(random.randint(0,1))
    code.append(codeword)
    print(codeword)


