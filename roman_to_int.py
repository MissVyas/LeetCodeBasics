class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        arr=[]
        
        for ch in s:
            if len(arr) == 0:
                arr.append(roman_dict[ch])
            else:
                if (arr[-1] >= roman_dict[ch]):
                    arr.append(roman_dict[ch])
                else:
                    arr[-1] = roman_dict[ch] - arr[-1]
        
        return sum(arr)

res = Solution().romanToInt("MMMCMXCIX")
print res
