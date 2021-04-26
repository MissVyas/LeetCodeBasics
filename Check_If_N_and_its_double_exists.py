class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Constraints
        # 1. i != j
        # 2. 0 <= i, j < arr.length
        # 3. arr[i] == 2 ** arr[j]
        # 4. 2 <= arr.length <= 500
        # 5. -10^3 <= arr[i] <= 10^3

        for i in arr:
            if arr.count(2 * i) != 0 and i != 0:
                return True
            elif i == 0  and arr.count(0) > 1:
                return True
            else:
                continue

        return False

#res = Solution().checkIfExist([0,0])
#print res