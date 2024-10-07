class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev=-1
        while prev != len(s):
            prev = len(s)
            s = s.replace("AB", "").replace("CD", "")
        return len(s)