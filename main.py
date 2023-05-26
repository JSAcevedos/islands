from collections import deque

class node:
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None

Q = deque()

def insertValue(data, root):
	newnode = node(data)
	if Q:
		temp = Q[0]
	if root == None:
		root = newnode
		
	elif temp.left == None:
		temp.left = newnode

	elif temp.right == None:
		temp.right = newnode
		temp = Q.popleft()
	
	Q.append(newnode)
	return root

def createTree(a, root):
	for i in range(len(a)):
		root = insertValue(a[i], root)
	return root

def levelOrder(root):
	Q = deque()
	Q.append(root)
	while Q:
		temp = Q.popleft()
		if temp.left != None:
			Q.append(temp.left)
		if temp.right != None:
			Q.append(temp.right)

def preorder_traversal(tree, n):
	if tree is None:
		return []

	results = []
	if tree.data != -1:
		results.append(tree.data)
	results += preorder_traversal(tree.left, n - 1)
	results += preorder_traversal(tree.right, n - 1)

	return results[:n]


def inorder_traversal(tree, n):
	if tree is None:
		return []

	results = []
	if tree.data != -1:
		results += inorder_traversal(tree.left, n)
		results.append(tree.data)
	results += inorder_traversal(tree.right, n - 1)

	return results[:n]


def postorder_traversal(tree, n):
	if tree is None:
		return []

	results = []
	if tree.data != -1:
		results += postorder_traversal(tree.left, n)
		results += postorder_traversal(tree.right, n)
		results.append(tree.data)

	return results[:n]


a = input().split()
b = []
for i in a:
	b.append(int(i))

a = int(input())

root = None
root = createTree(b, root)
levelOrder(root)

x = preorder_traversal(root,a)
y = inorder_traversal(root,a)
z = postorder_traversal(root,a)

pre = ["Preorder", 0]
ino = ["Inorder", 0]
pos = ["Postorder", 0]

for i in range(a):
	pre[1] += x[i]
	ino[1] += y[i]
	pos[1] += z[i]

max = max(pre[1],ino[1],pos[1])
if max == pre[1]:
	print(pre[0], max, end="")
elif max == ino[1]:
	print(ino[0],max, end="")
else:
	print(pos[0],max, end="")