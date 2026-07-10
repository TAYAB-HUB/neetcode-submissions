class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return chr(257)
        r = []
        for i in strs:
            r.append(str(len(i)))
            r.append(',')
        r.append('#')
        for i in strs:
            r.append(i)
        return ''.join(r)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s == chr(257):
            return []
        si, r, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            si.append(int(s[i:j]))
            i = j + 1
        i += 1
        for s1 in si:
            r.append(s[i:i + s1])
            i += s1
        return r
