class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        from itertools import permutations
        seen= set()
        for i in permutations(digits, 3):
            f, m, l= i
            if f == 0:
                continue
            if l%2 != 0:
                continue
            num= 100*f+10*m+l
            seen.add(num)
        return len(seen)