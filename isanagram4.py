from collections import Counter


class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        if sorted(s) != sorted(t):
            return False
        return True


res = Solution().isAnagram("test", "ttes")
print res
