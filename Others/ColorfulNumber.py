class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        s = str(A)
        n = len(s)
        hs = set()
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod = prod * int(s[j])
                if prod not in hs:
                    hs.add(prod)
                else:
                    return 0
        return 1

obj = Solution().colorful(1234)
print(obj)

