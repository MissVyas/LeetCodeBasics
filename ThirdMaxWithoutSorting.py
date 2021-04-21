class Solution:
    def thirdMax(self, nums):
        set_nums = set(nums)
        if len(set_nums) < 3:
            return max(set_nums)
        set_nums.remove(max(set_nums))
        set_nums.remove(max(set_nums))
        return max(set(set_nums))


res = Solution().thirdMax([2,2,3,1])
print res