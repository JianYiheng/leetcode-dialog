from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        TreeList = [root]

        while 1:
            ptr_node = TreeList.pop(0)
            if ptr_node is None:
                if not TreeList:
                    break
                else:
                    continue
            ptr_temp = ptr_node.left
            ptr_node.left = ptr_node.right
            ptr_node.right = ptr_temp
            TreeList.append(ptr_node.left)
            TreeList.append(ptr_node.right)
        return root


