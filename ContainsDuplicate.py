class Solution:
    def containsDuplicate(self, nums):
        sorted_nums = sorted(nums)
        #print(sorted_nums)
        unique_nums = sorted(list(set(nums)))
        #print(unique_nums)

        if sorted_nums == unique_nums:
            return False
        else:
            return True

res = Solution().containsDuplicate([1,5,-2,-4,0])
print res