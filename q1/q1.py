#Question 1: Huffman encoding
# Google Colab link : https://colab.research.google.com/drive/1vPDOm3tLWidE3P3zH8vqES93pp6aj-Bx?usp=sharing

import time
import math


# defining a class object for the node in Huffman tree
class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
# initializing encoding and decoding tables/Python Dictionaries
encode = {}
decode = {}

# Function to check if the given strings are same or different
def checkDiff(decoded, data):
    if(decoded==data):
        print("Input string and decoded string are same\n")
    else:
        print("Input string and decoded string are different\n")

# Recursive function to get codewords for symbols given the Huffman tree
def Map(node,st):
    if node.right!=None:
        Map(node.right,st+'0')
    if node.left!=None:
        Map(node.left,st+'1')
    if node.right==None and node.left==None:
        encode[node.val] = st
        decode[st] = node.val
#        print(node.val, st)


# Input file
#filename = input()
print("Enter name of input file\n(Use one of the 3 test files provided)")
filename = input()
outputfile = input("Enter the name of output file: ")
decodedfile = input("Enter the name of decoded file: ")
print("\n")
# Reading the input file
textFile = open(filename, "r")
data = textFile.read()
data = data[:-1]

start_time = time.time()
# going through the input file and building the frequency table
freq = {}
for r in range(len(data)):
    k = data[r]
    if k in freq:
        freq[k] += 1
    else:
        freq[k] = 1

N = len(freq)

freq = dict(sorted(freq.items(), key=lambda item: item[1]));
#print(freq)

tab = {}
for r in freq.keys():
    k = Node(r);
    tab[k] = freq[r];

#print(tab)

# Constructing the Huffman tree based on the frequency table
root = None
for i in range(N-1):
    tab = dict(sorted(tab.items(), key=lambda item: item[1]));
    nodes = list(tab.keys());
    Lnode = nodes[0];
    Rnode = nodes[1];
    values = list(tab.values());
    sum1 = values[0]+values[1];
    curNode = Node(sum1);
    curNode.left = Lnode;
    curNode.right = Rnode;
    tab.pop(Lnode);
    tab.pop(Rnode);
    tab[curNode] = sum1;
    root = curNode;
#    print(sum1)

# Calling Map function to get encode and decode tables from Huffman tree
Map(root,"")
#print(code)
#print(root.right.val, root.left.left.val)

output = "";
for r in range(len(data)):
    output += encode[data[r]]
# Writing Encoded string to a file
filep = open(outputfile, "w")
filep.write(output)
print("Encoded string written to " + outputfile)
#print(decode)

# Reconstructing the input file from the decoding map
outlen = len(output)
cur = 0
dec = ""
for i in range(outlen+1):
    if output[cur:i] in decode:
        dec += decode[output[cur:i]]
        cur = i
#print(data)
#print(dec)
# Checking the difference between Input string and reconstructed string
checkDiff(dec,data)

filep = open(decodedfile, "w")
filep.write(dec)
print("Decoded string written to " + decodedfile)
print("\n")
print("Execution time: %s seconds" % (time.time() - start_time))
len1 = len(output)
len2 = len(data)*math.ceil(math.log2(N))
print("\n")
print("No of characters(Size) in encoded string :" , len1)
print("No of characters(Size) required to encode using a naive algorithm :",len2)
print("Ratio :" , len1/len2)
print("\n")
print("Enter 1 to print the encoding map\nEnter 2 to print the endoded string\nEnter 3 to exit")
x = input()

while(x!="3"):
    if x=="1":
        print("Code:")
        for r in encode:
            print(r,' --- ', encode[r])
    if x=="2":
        print("Encoded String:\n",output)
    x = input()
