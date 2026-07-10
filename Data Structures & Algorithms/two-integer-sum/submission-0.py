class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        for j in range(1,len(nums)):
            if(nums[j]+nums[i]==target):
                return [i,j]
                j+=1

        