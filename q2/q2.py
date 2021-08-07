#This is an interactive program. The user has to give the values for n,k,p while running based on the instructions given by the code

#For the code used in plotting the additional plots and for the video presentation please
#check this link
#https://colab.research.google.com/drive/107lmFO7yYChbdyToJXiDzYSVsL8xlzke?usp=sharing

#Question 2: Error Probability of Random Codes over a BSC

import random
import numpy as np
import matplotlib.pyplot as plt

def randomCodeConstructor(List): #Function to generate 2^k random codewords from {0,1}^n
    
    #Obtaining values of n,k,p from the list passed as parameter
    n = List[0]
    k = List[1]
    p = List[2]

    #codeC used to store the codewords generated 
    codeC = []

    #Variable to store the number of codewords generated
    cnt = 0
   
    while(cnt < (2**k)): #Run a loop till we get 2^k codewords
        codeword = [] #Initializing codeword array to store the generated codeword in current iteration
        
        for length in range(n): #Run random.randint(0, 1) n times to get a codeword of length n made of 0s and 1s
            codeword.append(random.randint(0, 1)) #random.randint(0, 1) generates 0 OR 1 randomly
        
        if codeword not in codeC: #Condition to check if the codeword is present in C (code)
            codeC.append(codeword)
            cnt += 1
    return codeC

def BSC(transmittedCodeword, p): #BSC function to simulate working of Binary Symmetric Channel, takes parameters as the codeword and the bit-flip probability (p)
    
    n = len(transmittedCodeword)
    receivedCodeword = [0]*n #Intialize a n length vector of zeros, to store the output of the Binary Symmetric Channel
    

    #Working: For every bit in the transmitted codeword, we generate a random probability. 
    #If the probability of that bit is less than to the bit flip probability, we invert the bit
    #If the probability of that bit is greater than or equal to bit flip probability, we pass the bit as it is (no flipping)
    
    for i in range(n): 
        probabilityofBit = random.random() #Generates a random number between 0 to 1

        if(probabilityofBit < p): #If the probability of that bit is less than to the bit flip probability,
            #Bit Flip Operation
            if(transmittedCodeword[i] == 0): #if bit is 0, 0 is flipped to 1
                receivedCodeword[i] = 1
            elif(transmittedCodeword[i] == 1): #if bit is 1, 1 is flipped to 0
                receivedCodeword[i] = 0
        else:
            receivedCodeword[i] = transmittedCodeword[i]

    return receivedCodeword

def minimumDistanceDecodingAlgorithm(transmittedCodeword,receivedCodeword, codeC):
    
    n = len(receivedCodeword)
    minimumHammingDistance = n #Assigning the maximum hamming distance between two vectors, when all the bits are different
    
    estimateCodewordIndex = 0
    E = 0

    for t in range(len(codeC)):  # Iterating through all codewords in C to compare which codeword has minimum hamming distance with Received Codeword
        hammingDistance = 0
        
        for ind in range(n):
            if(receivedCodeword[ind] != codeC[t][ind]): #Comparing the index of bit ind in the t th codeword
                hammingDistance += 1
        
        if hammingDistance < minimumHammingDistance:  # If current hamming Distance obtained is lesser than stored difference,
            estimateCodewordIndex = t  # store the index of the new difference
            minimumHammingDistance = hammingDistance  # we update the minimum difference
    
    estimateCodeword = codeC[estimateCodewordIndex]
    
    if(estimateCodeword != transmittedCodeword):  # If the estimated codeword does not match the input codeword, we increment error
        E += 1  # E - Number of errors in decoding by the decoding algorithm
    
    return E


def decoding(codeC, data):
    n = data[0]
    k = data[1]
    p = data[2]

    N = 100

    totalError = 0
    minimumProbabilityOfError = 1000 #whats the max value of E/N = k/N ?

    for i in range(N):
        #codewordIndex = random.randint(0, (2**k-1)
        #transmittedCodeword = codeC[codewordIndex]

        cur = random.randint(0, (2**k)-1)
        c = codeC[cur]
        transmittedCodeword = c

        bitFlipProbability = p
        receivedCodeword = BSC(transmittedCodeword, bitFlipProbability)

        totalError = totalError +  minimumDistanceDecodingAlgorithm(transmittedCodeword,receivedCodeword, codeC)

    probabilityOfError = totalError / N
    return probabilityOfError

#Data Array to store the user-input for (n,k,p)
data = []

#Taking user input for (n,k,p)
print('Enter value for n')
n = int(input())
data.append(n)

print('Enter value for k')
k = int(input())
data.append(k)

print('Enter value for p')
p = float(input())
data.append(p)

#Assigning a large value temporarily for minimum Probability Of Error
#minimumProbabilityOfError is updated when we get a code with lower probability
minimumProbabilityOfError = 10
      
#Running the c0ode 5 times for 5 trials
for j in range(5):
    #Part 1: Random Code Construction
    #randomCodeConstructor generates a random code of 2^k codewords, each of length n
    codeC = randomCodeConstructor(data)

    #Part 2: Decoding
    #decoding function Calls BSC and decodes the recieved codeword from BSC
    probabilityOfError = decoding(codeC, data)

    #Updating minimumProbabilityOfError
    minimumProbabilityOfError = min(minimumProbabilityOfError, probabilityOfError)

print('The minimum probability of Error for n = ' , n , ' k = ' , k , ' p = ' , p)
print ('%.3f' % minimumProbabilityOfError)
print('\n')
