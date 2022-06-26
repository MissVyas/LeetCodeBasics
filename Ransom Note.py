from collections import Counter


class Solution:
    def canConstruct(self, ransomNote, magazine):
        return Counter(ransomNote) <= Counter(magazine)


res = Solution().canConstruct('test', 'adbtestck')
print(res)
