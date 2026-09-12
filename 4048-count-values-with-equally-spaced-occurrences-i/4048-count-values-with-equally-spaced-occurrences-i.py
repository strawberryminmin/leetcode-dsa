class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count= 0
        for x in set(nums):
            if nums.count(x) == 3:
                i1= nums.index(x)
                i2= nums.index(x, i1 + 1)
                i3= nums.index(x, i2+ 1)

                if i2-i1 == i3-i2:
                    count +=1
        return count