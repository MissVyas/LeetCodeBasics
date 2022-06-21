class Solution:
    def merge(self, A, m, B, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m:
            if A[i] > B[j]:
                tmp = A[i]
                A[i] = B[j]
                B[j] = tmp
                B.sort()
                i = i + 1
            elif A[i] < B[j]:
                i = i + 1
            else:
                pass

        print A+B

Solution().merge([1, 3, 4], 3, [2, 5, 6], 3)

# Leet code time level exceed
# TC: O(n+m)
# SC: O(1)


