class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n=len(strs)
        if n==0:
            return ""
        cp=strs[0]
        for i in range(1,n):
            while cp !=strs[i][:len(cp)]:
                cp=cp[:-1]
                if cp=="":
                    return ""
        return cp
