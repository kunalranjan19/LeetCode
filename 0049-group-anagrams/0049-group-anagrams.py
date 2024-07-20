class Solution(object):
    def groupAnagrams(self, strs):
        mp={}
        for s in strs:
            sort="".join(sorted(s))
            if sort not in mp:
                mp[sort]=[]
            mp[sort].append(s)
        return list(mp.values())