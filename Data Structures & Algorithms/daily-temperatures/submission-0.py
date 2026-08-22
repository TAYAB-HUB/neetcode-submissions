class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []

        for i,ti in enumerate(temp):
            while stack and temp[stack[-1]] < ti:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res