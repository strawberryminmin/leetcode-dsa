class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen= set()
        left= 0
        maxlength= 0
        for right, i in enumerate(s):
            while i in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxlength= max(maxlength, right- left +1)
        return maxlength