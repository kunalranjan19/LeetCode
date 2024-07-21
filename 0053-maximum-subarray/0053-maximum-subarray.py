class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        n=len(nums)
        maxi=-2**31
        for i in range(0,n,1):
            sum+=nums[i]
            if sum > maxi:
                maxi=sum
            if sum < 0:
                sum=0
        return maxi

        