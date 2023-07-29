class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countpalindrome(s, i, i)
            res += self.countpalindrome(s, i, i+1)
        return res
    def countpalindrome(self, s, l, r):
        res1 = 0
        while (l >= 0 and r < len(s)) and s[l] == s[r]:
            res1 += 1
            l -= 1
            r += 1
        return res1

