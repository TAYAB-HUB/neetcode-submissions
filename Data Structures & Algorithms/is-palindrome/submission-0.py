class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = [char.lower()for char in s if char.isalnum()]
        t = "".join(c)
        u = "".join(reversed(c))
        if t==u:
            i = True
        else:
            i = False
        return i
        