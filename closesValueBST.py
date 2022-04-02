''' We need to find the closest value of a target value in a BST
		10
	   /  \
	 5      15
	/ \    /  \
   2   5  13   22
  / 		\
 1 			 14

target = 12
o/p: 13


'''

def closesValueBST(tree, target):
	return closesValueBSTHelper(tree, target, float('inf'))

# ---------------Interative Method ------------------------------------

def closesValueBSTHelper(tree, target, closest):
	currentNode = tree
	while currentNode:
		if tree is None:
			return closest
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return closest

# ---------------Reccurssive Method ------------------------------------
def closesValueBSTHelper(tree, target, closest):
	currentNode = tree
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - currentNode.value):
		closest = currentNode.value
	if target < currentNode.value:
		closesValueBSTHelper(currentNode.left, target, closest)
	elif target > currentNode.value:
		closesValueBSTHelper(currentNode.right, target, closest)
	else:
		return closest