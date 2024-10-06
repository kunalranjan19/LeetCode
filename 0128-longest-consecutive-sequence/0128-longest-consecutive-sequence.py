class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        if not nums:
            return 0
        res=[nums[0]]
        count=1
        for i in range(n-1):
            if nums[i]+1==nums[i+1]:
                res.append(nums[i+1])
            elif nums[i] != nums[i + 1]:  
                count = max(count, len(res))  
                res = [nums[i + 1]]
        
        count = max(count, len(res))
        return count
