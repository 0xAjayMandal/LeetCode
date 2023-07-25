class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = [int(i) for i in range(-1000, 1001)]
        return ans[1000 + a+b]