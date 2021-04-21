import itertools


class Solution(object):
    def buddyStrings(self,A,B):

        # check first
        if len(a) != len(b):
            return False

        # check two
        if A == B:
            seen = set()
            for ele in A:
                if ele in seen:
                    return True
                else:
                    seen.add(ele)
            return False

        # Check three
        if A != B:
            pairs = []

            for a, b in itertools.izip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

res = Solution().buddyString('ab','ab')
print res








