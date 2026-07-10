class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a,s,p = [1]*len(nums),1,1
        for i in range(len(nums)):
            a[i]*=s
            s *=nums[i]
            a[-1-i] *=p
            p *= nums[-1-i]
        return a
        