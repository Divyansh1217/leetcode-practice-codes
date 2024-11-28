class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        a=defaultdict(list)
        for i in strs:
            s=''.join(sorted(i))
            a[s].append(i)
        return list(a.values())