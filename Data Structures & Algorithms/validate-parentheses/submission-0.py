class Solution:
    def isValid(self, s: str) -> bool:
        v = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        b = []

        for c in s:
            if c in v:
                if not b:
                    return False
                top = b.pop()
                if v[c]!=top:
                    return False
            else:
                b.append(c)
        if b:
            return False
        else:
            return True

        