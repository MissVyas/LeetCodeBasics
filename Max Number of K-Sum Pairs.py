class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        p1 = 0
        p2 = len(nums) - 1
        ans = 0

        while (p1 < p2):
            sum1 = nums[p1] + nums[p2]
            if sum1 == k:
                p1 += 1
                p2 -= 1
                ans += 1
            elif sum1 > k:
                p2 -= 1
            elif sum1 < k:
                p1 += 1

        return ans


obj = Solution()
print(obj.maxOperations([3,1,5,1,1,1,1,1,2,2,3,2,2],1))



