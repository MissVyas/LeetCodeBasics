class Solution:
    def maxSubArray(self, nums):
        cur = nums[0]
        ret = cur
        for num in nums[1:]:
            cur = max(num, cur + num)
            ret = max(ret, cur)
            if ret < 0:
                ret = 0
        return ret


# TC: O(n)
# SC: O(1)
# Kadane's Algorithm

res = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print res
