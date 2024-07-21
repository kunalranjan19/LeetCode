class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        hsh={}
        for num in nums:
            hsh[num]=hsh.get(num,0)+1
            if hsh[num]>length/2:
                return num