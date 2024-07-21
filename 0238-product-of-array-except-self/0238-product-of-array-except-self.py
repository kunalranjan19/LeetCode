class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length=len(nums)
        mul=[1]*length
        for i in range(1,length):
            mul[i]=mul[i-1]*nums[i-1]
        ar=nums[-1]
        for i in range(length-2,-1,-1):
            mul[i]*=ar
            ar*=nums[i]
        return mul
        