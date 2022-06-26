from collections import Counter


class Solution:
    def canConstruct(self, ransomNote, magazine):
        randict = {}

        for s in ransomNote:
            if s not in randict.keys():
                randict[s] = 1
            else:
                randict[s] += 1
        #print(randict)

        magict = {}

        for c in magazine:
            if c not in magict.keys():
                magict[c] = 1
            else:
                magict[c] += 1
        #print(magict)

        for k, v in randict.items():
            if k not in randict.keys():
                return False
            if v > magict[k]:
                return False
        return True


res = Solution().canConstruct('aa','aabb')
print(res)
