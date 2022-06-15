class Solution(object):
    def RemoveElement(self, num, val):
        i=0
        j=0
        while j<len(num):
            if num[j] != val:
                num[i] = num[j]
                i= i + 1
            j = j + 1
        return i



res = Solution().RemoveElement([1, 1, 2, 2, 2, 2],2)
print(res)
