class Solution:
    def findMin(self, nums: List[int]) -> int:
        first, last = 0, len(nums)-1
        result = nums[0]
        while first <= last:
            if nums[first] < nums[last]:
                result = min(result, nums[first])
                break
            mid = (first+last) //2
            result = min(result, nums[mid])
            if nums[mid] >= nums[first]:
                first = mid+1
            else:
                last = mid -1
        return result