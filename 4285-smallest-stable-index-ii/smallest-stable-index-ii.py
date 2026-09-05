class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n= len(nums)
        arr= [0] * n
        arr[n-1]= nums[n-1]
        for i in range(n-2, -1, -1):
            arr[i]= min(arr[i+1], nums[i])
        maxx= nums[0]
        for i in range(n):
            maxx= max(maxx, nums[i])
            if maxx - arr[i]<= k:
                return i
        return -1