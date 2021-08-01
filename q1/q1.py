class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

encode = {}
decode = {}

def checkDiff(decoded, data):
    if(decoded==data):
        print("Strings are same")
    else:
        print("Strings are different")

def Map(node,st):
    if node.right!=None:
        Map(node.right,st+'0')
    if node.left!=None:
        Map(node.left,st+'1')
    if node.right==None and node.left==None:
        encode[node.val] = st
        decode[st] = node.val
#        print(node.val, st)

filename = "file1.txt"

textFile = open(filename, "r")
data = textFile.read()
data = data[:-1]
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

Map(root,"")
#print(code)
#print(root.right.val, root.left.left.val)
print("Code:")
for r in encode:
    print(r,' --- ', encode[r])
output = "";
for r in range(len(data)):
    output += encode[data[r]]
#print("Encoded String: ",output)
filep = open("encoded.txt", "w")
filep.write(output)
print("Encoded string written to encoded.txt")
#print(decode)

outlen = len(output)
cur = 0
dec = ""
for i in range(outlen+1):
    if output[cur:i] in decode:
        dec += decode[output[cur:i]]
        cur = i
#print(data)
#print(dec)
checkDiff(dec,data)
