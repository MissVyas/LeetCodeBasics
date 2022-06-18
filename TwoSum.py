class Solution:
        def twoSum(self, nums, target):
            for i in range(len(nums)):
                rem = target - nums[i]
                if rem in nums[i+1:]:
                    return[i,nums.index(rem,i+1)] #[3,3]


res = Solution().twoSum([3,2,4],6)
print res
