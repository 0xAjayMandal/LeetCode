class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        CurrentMax, CurrentMin = 1, 1
        result = nums[0]

        for i in nums:
            value = (i, i*CurrentMax, i*CurrentMin)
            CurrentMax, CurrentMin = max(value), min(value)
            result = max(result, CurrentMax)
        return result