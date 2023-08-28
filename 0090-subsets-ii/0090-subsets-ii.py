class Solution:
    def subsetsWithDup(self, lst: List[int]) -> List[List[int]]:
        pw_set = [[]]

        for i in range(0,len(lst)):
            for j in range(0,len(pw_set)):
                ele = pw_set[j].copy()
                ele = ele + [lst[i]]
                pw_set = pw_set + [ele]

        a= list(set(tuple(sorted(sub))for sub in pw_set ))
        return a