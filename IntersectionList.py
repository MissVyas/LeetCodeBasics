class Solution:
    def intersect(self, nums1, nums2):
        m = {} # to maintain duplicate keys
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1 # we want to iterate to bigger data
        for i in nums1:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        result = []
        for i in nums2:
            if i in m and m[i]:
                m[i] -= 1
                result.append(i)
        return result

res = Solution().intersect([1,4,5,3,6],[2,3,5,7,9])
print res