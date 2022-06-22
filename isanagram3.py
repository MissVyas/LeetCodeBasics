from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        unq_char = set(t)

        if len(s) != len(t):
            return False

        for i in unq_char:
            if t.count(i) != s.count(i):  # counts the number of objects over here
                return False
        return True


res = Solution().isAnagram("test", "ttes")
print res
