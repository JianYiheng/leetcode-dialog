from typing import List
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.n = 0

    def generateTrees(self, n: int) -> List[TreeNode]:
        self.n = n
        if n == 0:
            return []
        count = 1
        listNode = []
        for num in range(1, self.n+1):
            root = TreeNode(num)
            self.funcReverse(count, listNode, root)

        return listNode

    def funcReverse(self, count: int, listNode: List[TreeNode], root: TreeNode) -> None:
        if count == self.n:
            listNode.append(copy.deepcopy(root))
            return

        node = root

        for num in range(1, self.n+1):
            if num < node.val:
                if not node.left:
                    node.left = TreeNode(num)
                    self.funcReverse(count+1, listNode, root)
                    node.left = None
                    continue
                node = node.left
            elif num > node.val:
                if not node.right:
                    node.right = TreeNode(num)
                    self.funcReverse(count+1, listNode, root)
                    node.right = None
                    continue
                node = node.right
            else:
                pass
        return


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
    ret = Solution().generateTrees(5)
    for i in ret:
        print(TreeNode2String(i))
