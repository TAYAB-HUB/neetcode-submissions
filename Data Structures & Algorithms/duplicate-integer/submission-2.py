class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        m = len(nums)
        if len(nums) <= 1:
            return False
        for i in range(m - 1):
            if nums[i] == nums[i + 1]:
                return True
   
        return False