class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)
            n >>= 1
        return result


if __name__=='__main__':
    ret = Solution().reverseBits(0b11111111111111111111111111111101)
    print(ret, bin(ret))