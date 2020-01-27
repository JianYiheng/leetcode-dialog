from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        listQueue = [root]
        listBan = [None, root]
        listPath = [root.val]
        while listQueue:
            node = listQueue[-1]
            if node.left not in listBan:
                listQueue.append(node.left)
                listBan.append(node.left)
                listPath.append(node.left.val)
            elif node.right not in listBan:
                listQueue.append(node.right)
                listBan.append(node.right)
                listPath.append(node.right.val)
            else:
                listQueue.pop()
                if node.left is None and node.right is None:
                    print(listPath)
                listPath.pop()
        return 10


def String2TreeNode(input: List) -> TreeNode:
    if len(input) == 1:
        return TreeNode(input[0])

    index = 1
    node_root = TreeNode(input[0])
    node_queue = [node_root]

    while index < len(input):
        value = input[index]
        node = node_queue.pop(0)
        if value != 'null':
            node_new = TreeNode(value)
            node.left = node_new
            node_queue.append(node_new)
        index += 1
        if index >= len(input):
            break
        value = input[index]
        index += 1
        if value != 'null':
            node_new = TreeNode(value)
            node.right = node_new
            node_queue.append(node_new)
    return node_root


if __name__=='__main__':
    input_list = [10, 5, -3, 3, 2, 'null', 11, 3, -2, 'null', 1]
    input_root = String2TreeNode(input_list)
    ret = Solution().pathSum(input_root, 10)
    print(ret)

