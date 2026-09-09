class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        for i in range(1,17):
            lo=10**(i-1)
            hi=min(10**i-1,n)
            if lo>n:
                break
            total+=(hi-lo+1)*((i-1)//3)
        return total