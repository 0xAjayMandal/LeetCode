class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverse_table = dict()
        for i in range(len(nums)):
            second_target = target - nums[i]
            if second_target in reverse_table:
                return [reverse_table[second_target],i]
            else:
                reverse_table[nums[i]] =i