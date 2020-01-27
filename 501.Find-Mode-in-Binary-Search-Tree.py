from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        listQueue = [root]
        list
        listBan = []
        while listQueue:



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


def TreeNode2String(input: TreeNode) -> List:
    listQueue = [input]
    output = [input.val]
    while listQueue:
        node = listQueue.pop(0)
        if node.left:
            listQueue.append(node.left)
            output.append(node.left.val)
        elif node.right:
            output.append('null')

        if node.right:
            listQueue.append(node.right)
            output.append(node.right.val)

    return output


if __name__ == '__main__':
    x = String2TreeNode([1,'null',2,2])
    ret = Solution().findMode(x)
    print(ret)
