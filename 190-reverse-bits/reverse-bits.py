class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # Since the bits are 32bits integer
        for i in range(32):
            bit = (n>>i)&1
            res = res | (bit << (31-i))
        return res
