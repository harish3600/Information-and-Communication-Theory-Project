class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

code = {}
def Encode(node,st):
    if node.right!=None:
        Encode(node.right,st+'0')
    if node.left!=None:
        Encode(node.left,st+'1')
    if node.right==None and node.left==None:
        code[node.val] = st
#        print(node.val, st)

filename = "test.txt"

textFile = open(filename, "r")
data = textFile.read()
freq = {}
for r in range(len(data)-1):
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

Encode(root,"")
#print(code)
#print(root.right.val, root.left.left.val)
print("Code:")
for r in code:
    print(r,' --- ', code[r])
output = "";
for r in range(len(data)-1):
    output += code[data[r]]
#print("Encoded String: ",output)
filep = open("encoded.ari", "w")
filep.write(output)
print("Encoded string written to encoded")
