class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        ans = 0
        left = 0
        for right in range(len(s)):
            hm[s[right]] = 1 + hm.get(s[right], 0)
            while (right-left+1) - max(hm.values()) > k:
                hm[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans 