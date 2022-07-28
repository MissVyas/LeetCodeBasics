class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    # Solution is done using hasing
    def dNums(self, A, B):
        N = len(A)

    hashmap = {}
    res = []

    for i in range(B):
        if A[i] not in hashmap:
            hashmap[A[i]] = 1
        else:
            hashmap[A[i]] += 1

    res.append(len(hashmap))

    for i in range(N - B):
        if A[i] in hashmap:
            if hashmap[A[i]] == 1:
                del [hashmap[A[i]]]
            else:
                hashmap[A[i]] -= 1

        if A[i + B] not in hashmap:
            hashmap[A[i + B]] = 1
        else:
            hashmap[A[i + B]] += 1

        res.append(len(hashmap))

    return res



