class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        pow=1
        if n<0:
            x= 1/x
            n=abs(n)
        while n:
            if n%2 ==1:
                pow*=x
                n=n-1
            else:
                x= x*x
                n=n//2
        if x < 0 and n % 2!=0:
            pow= -abs(pow)
        return pow