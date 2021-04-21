class Solution(object):
    def thridMax(self,nums):
        """

        :param nums: List[int]
        :return: int
        """

        setnums = set(nums)
        sortedset = sorted(setnums,reverse=True)

        if len(sortedset) < 3:
            return sortedset[0]
        else:
            return sortedset[2]

res = Solution().thridMax([2,2,3,1])
print res