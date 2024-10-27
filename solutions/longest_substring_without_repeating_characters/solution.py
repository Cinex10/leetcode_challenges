class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = ''
        b = 0
        m = 0
        for idx, c in enumerate(s):
            if c not in r:
                r += c
                b += 1
            else:
                i = r.index(c) + 1
                r = r[i:] + c
                b = len(r)
            m = max(m,b)
        return  m
    
# pwwkew