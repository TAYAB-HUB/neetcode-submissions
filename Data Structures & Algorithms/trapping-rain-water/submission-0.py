class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        e = len(height)-1

        l,r,t = 0,0,0

        while s<e:
            l = max(l,height[s])
            r = max(r,height[e])

            if l < r:
                t+= l-height[s]
                s+=1
            else:
                t+= r-height[e]
                e-=1
        return t