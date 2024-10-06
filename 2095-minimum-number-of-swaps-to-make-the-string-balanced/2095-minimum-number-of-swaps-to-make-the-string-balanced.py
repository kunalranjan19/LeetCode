class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        close, maxc=0,0
        for c in s:
            if c=="[":
                close-=1
            else:
                close+=1
            maxc=max(close, maxc)
        swaps=(maxc+1)//2
        return swaps