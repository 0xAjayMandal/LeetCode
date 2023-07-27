class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i, s in enumerate(strs):
            count = [0] * 26
            for char in s:
                #Incrementing by using ASCII values
                count[ord(char) - ord("a")] += 1
            sorted_str = tuple(count)
            hashmap.setdefault(sorted_str, []).append(i)
        return [[strs[i] for i in group] for group in hashmap.values()]