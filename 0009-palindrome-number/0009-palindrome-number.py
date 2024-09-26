class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev=0
        d=x
        while(x>0):
            a=x%10
            rev=(rev*10) +a
            x=x//10
        if d==rev:
            return True
        else:
            return False