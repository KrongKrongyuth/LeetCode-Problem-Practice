class Solution(object):
    def lengthOfLongestSubstring(self, s) :
        if s.isalpha() and len(s) > 1 :
            max_word = 0
            for i in range(len(s)) :
                current_word = ""
                for j in range(len(s[i:])) :
                    starter = s[i+j]
                    if starter not in current_word : 
                        current_word += starter
                        len_current = len(current_word)
                        if len_current >= max_word : max_word = len_current
                    else :
                        break
            return max_word
        else : return len(set(s))

s = 'pwwkew'
print(Solution().lengthOfLongestSubstring(s))