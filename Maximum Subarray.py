class Solution:
    def maxSubArray(self, nums):
        max_sum = 0
        cur_sum = nums[0]
        i = 0
        while i < len(nums):
            if cur_sum >= 0:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]

            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum


# TC: O(n)
# SC: O(1)

res = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print res
