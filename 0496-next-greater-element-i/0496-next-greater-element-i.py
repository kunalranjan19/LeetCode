class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r=[]
        for i in nums1:
            length=len(r)
            ind=nums2.index(i)
            for j in nums2[ind:]:
                if j>i:
                    r.append(j)
                    break
            if len(r)==length:
                r.append(-1)
        return r      