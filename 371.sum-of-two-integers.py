import sys


class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        result_and = a & b  # carry
        result_xor = a ^ b  # sum
        while result_and:
            result_and = result_and & sys.maxsize
            result_and, result_xor = result_xor & (result_and << 1), result_xor ^ (result_and << 1)
        return result_xor


if __name__=='__main__':
    ret = Solution().getSum(-1, 1)
    print(ret)