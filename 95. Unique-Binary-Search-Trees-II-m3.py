from typing import List, Dict, Union
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[None]:
        if n == 0:
            return []

        dictDP: Dict[int, List] = {}
        for numRoot in range(1, n + 1):
            numLeft = numRoot - 1
            numRight = n - numRoot

            if numLeft == 0: dictDP[numLeft] = [None]
            if numRight == 0: dictDP[numRight] = [None]

            if numLeft not in dictDP.keys(): dictDP[numLeft] = []
            if numRight not in dictDP.keys(): dictDP[numRight] = []

            for nodeLeft in dictDP[numLeft]:
                for nodeRight in dictDP[numRight]:
                    nodeNew = TreeNode(numRoot)
                    nodeNew.left = nodeLeft
                    if not nodeRight:
                        nodeTemp = copy.deepcopy(nodeRight)
                        nodeNew.right = offsetClone(nodeRight, numRoot)
                    else:
                        nodeNew.right = nodeRight
                    dictDP[numRoot].append(nodeNew)
        return dictDP[n]


def offsetClone(nodeInput: TreeNode, offset: int) -> TreeNode:
    nodeQueue = [nodeInput]

    while nodeQueue:
        node = nodeQueue.pop(0)
        node.val += offset
        if node.left:
            nodeQueue.append(node.left)
        if node.right:
            nodeQueue.append(node.right)
    return nodeInput


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
