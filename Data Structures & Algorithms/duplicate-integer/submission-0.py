class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        m = len(nums)
        if len(nums)==1:
            return False
        for i in range(m):
            for j in range (i+1,m):
                if nums[i]==nums[j]:
                    return True
   
        return False 