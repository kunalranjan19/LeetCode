class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ind = sorted(range(n), key=lambda i: nums[i])
        min_index = float('inf')
        max_width = 0
        for i in ind:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)
    
        return max_width