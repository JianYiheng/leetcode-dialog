from typing import List
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        res = build_Trees(1, n)
        return res


def build_Trees(numLeft: int, numRight: int) -> List[TreeNode]:
    treeQueue = []
    if numLeft > numRight:
        return [None]
    for numRoot in range(numLeft, numRight + 1):
        tree_left = build_Trees(numLeft, numRoot - 1)
        tree_right = build_Trees(numRoot + 1, numRight)
        for nodeLeft in tree_left:
            for nodeRight in tree_right:
                treeCurr = TreeNode(numRoot)  # 注意这里的 创建node 不能放在循环外
                treeCurr.left = nodeLeft  # 不然这里修改 left, right 时，已存入列表的node也会改变
                treeCurr.right = nodeRight
                treeQueue.append(treeCurr)
    return treeQueue


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
    ret = Solution().generateTrees(3)
    for i in ret:
        print(TreeNode2String(i))