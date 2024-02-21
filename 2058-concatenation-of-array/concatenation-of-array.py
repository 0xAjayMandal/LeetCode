class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArray = []
        for i in range(len(nums)):
            newArray.append(nums[i])
        newArray.extend(newArray)
        return newArray