class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for i in nums:
            c[i] = 1+c.get(i,0)

        s1 = sorted(c.keys(),key = lambda x: c[x],reverse=True )
        return s1[:k]
        