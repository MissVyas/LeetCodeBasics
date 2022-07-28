class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        n = len(A)

    if B > n:
        return []

    ans = []
    for i in range(0, n):
        j = i + B - 1
        if j < n:
            count = len(set(A[i:j + 1]))
            ans.append(count)
        else:
            break
    return ans


