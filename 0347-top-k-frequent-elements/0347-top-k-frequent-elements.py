class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts=Counter(nums)
        ans=[]
        for item, _ in counts.most_common(k):
                ans.append(item)
        return ans

