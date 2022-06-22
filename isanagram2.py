from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


res = Solution().isAnagram("test", "ttes")
print res
