class Solution:
        def twoSum(self, nums, target):
            i = 0
            n = len(nums)
            j = n - 1
            while i<j:
                if nums[i] + nums[j] == target:
                    return [i,j]
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    i += 1
            return []

res = Solution().twoSum([2,7,11,15],9)
print res
