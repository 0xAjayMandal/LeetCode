class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        result = 0
        left = 0
        freq  = 0
        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right], 0)
            freq = max(freq, hashmap[s[right]])
            if (right-left+1) - freq > k:
                hashmap[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result