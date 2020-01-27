from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        listStack = [root]
        listBan = [None, root]
        listOutput = []
        while listStack:
            node = listStack[-1]
            if node.left not in listBan:
                listStack.append(node.left)
                listBan.append(node.left)
            elif node.right not in listBan:
                listStack.append(node.right)
                listBan.append(node.right)
                listOutput.append(node.right)
            else:
                listOutput.append(listStack.pop())

