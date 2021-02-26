class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        smallest_word = ""
        min_word_len = strs[0]
        for word in strs:
            if len(word) <= min_word_len:
                min_word_len = len(word)
                smallest_word = word
        print "Smallest word is: "+smallest_word
        
        
        subset = []
        flag = 1
        len1 = len(smallest_word)
        for word in strs:
            if word == smallest_word:
                pass
            else:
                for ch in smallest_word:
                    if ch in word[:len1]:
                        if ch not in subset:
                            subset.append(ch)
                    else:
                        flag=0
                        if ch in subset:
                            subset.remove(ch)

        

        print "Got array as: "+str(subset)
        
        prefix=""
        if subset != []:
            for letter in subset:
                prefix = prefix + letter


        if flag == 1:
            return prefix
        else:
            return ""
                        

res = Solution().longestCommonPrefix(["dog","racecar","car"])
print res
