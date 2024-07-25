class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapp = {}
        sett = set()
        for i in range(len(s)):
            if s[i] in mapp:
                if mapp[s[i]] != t[i]:
                    return False
            else:
                if t[i] in sett:
                    return False
                mapp[s[i]] = t[i]
                sett.add(t[i])
        return True