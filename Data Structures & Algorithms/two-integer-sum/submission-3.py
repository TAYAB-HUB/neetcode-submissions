class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = len(nums)
        for i in range(m):
            for j in range(i + 1, m):
                if(nums[i]+nums[j]==target):
                    return [i,j]
