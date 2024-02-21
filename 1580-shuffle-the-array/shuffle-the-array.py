class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newArray = []
        for i in range(n):
            newArray.append(nums[i])
            newArray.append(nums[i+n])
        return newArray