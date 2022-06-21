class Solution:
    def merge(self,nums1, m, nums2, n):
        i = 0
        j = 0
        k = 0
        nums3 = [0]*(m+n)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                i = i + 1
            elif nums1[i] > nums2[j]:
                nums3[k] = nums2[j]
                j = j + 1
            k = k + 1

        while (i < n):
            nums3[k] = nums1[i]
            i = i + 1
            k = k + 1

        while (j < m):
            nums3[k] = nums2[j]
            j = j + 1
            k = k + 1

        print nums3

Solution().merge([1, 3, 4], 3, [2, 5, 6], 3)

