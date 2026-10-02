class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count= 0
        curr=0
        for j in nums:
            if j==1:
                curr+=1
                count= max(count, curr)
            else:
                curr=0
        return count
        