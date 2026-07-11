class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers)-1

        while s<e:
            t = numbers[s]+numbers[e]
            if t == target:
                return [s+1,e+1]
            elif t<target:
                s+=1
            else:
                e-=1
        return[-1,-1]
        