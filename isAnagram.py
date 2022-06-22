class Solution:
    def isAnagram(self, s, t):
        m = {}
        if len(s) < len(t):
            s, t = t, s

        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        for c1 in t:
            if c1 in m and m[c1]:
                m[c1] -= 1
        values = m.values()
        if sum(values) == 0:
            return True
        else:
            return False


res = Solution().isAnagram("test","ttes")
print res