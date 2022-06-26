class Solution:
    def firstUniqChar(self, s):
        for char in s:
            if s.count(char) == 1:
                return s.index(char)
        return -1


res = Solution().firstUniqChar('aabbc')
print res
