class Solution(object):
    def RemoveElement(self, num, val):
        while (True):
            if val in num:
                num.remove(val)
            else:
                return len(num)


res = Solution().RemoveElement([1, 1, 2, 2, 2, 2],2)
print(res)
