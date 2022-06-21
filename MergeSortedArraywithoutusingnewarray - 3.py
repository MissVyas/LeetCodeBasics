import math


class Solution:
    def merge(self, A, m, B, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total_len = m + n
        A = A + B
        gap_val = total_len
        while gap_val != 0:
            gap_val = gap_val // 2
            if gap_val % 2 != 0 and gap_val != 1:
                gap_val += 1
            if gap_val == 0:
                return A
            i = 0
            j = gap_val
            while j < total_len:
                if A[i] > A[j]:
                    tmp = A[i]
                    A[i] = A[j]
                    A[j] = tmp
                i = i + 1
                j = j + 1
        return A

res = Solution().merge([1, 3, 4], 3, [2, 5, 6], 3)
print res


# Leet code time level exceed
# TC: O(n+m)
# SC: O(1)
