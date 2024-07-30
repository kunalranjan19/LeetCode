class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0 
        r=len(s)-1

        while l < r:
            if(s[l]!=s[r]):
                sl, sr= s[l+ 1:r+ 1], s[l:r]
                return (sl==sl[::-1] or sr==sr[::-1])
            l =l+ 1
            r =r- 1
        return True