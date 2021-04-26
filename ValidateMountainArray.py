class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Constraints:
        # 1. array length is less than three then its not mountain array
        # 3. 0 < i < arr.length -1
        # 2. arr[0] < arr[i] < ... <arr[i-1] < arr[i]

        len_arr = len(arr)
        if len_arr >= 3:
            max_num = max(arr)
            count_max = arr.count(max_num)
            flag_min = 1
            flag_max = 1
            if count_max > 1:
                return False
            else:
                max_idx = arr.index(max_num)
                i = 0
                while i < max_idx:
                    if arr[i] < arr[i+1]:
                        flag_min = 0
                    else:
                        flag_min = 1
                        return False
                    i = i+1

                j = max_idx
                while j < len_arr-1:
                    if arr[j] > arr[j+1]:
                        flag_max = 0
                    else:
                        flag_max = 1
                        return False
                    j = j+1

                if flag_max+flag_min == 0:
                    return True
        else:
            return False

res = Solution().validMountainArray([3,7,6,4,3,0,1,0])
print res