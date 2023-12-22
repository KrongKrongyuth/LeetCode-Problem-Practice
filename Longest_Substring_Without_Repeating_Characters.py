class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s.isalpha() and len(s) > 1 :
            word_dict = {}
            for i in range(len(s)) :
                current_word = ""
                for j in range(len(s[i:])) :
                    starter = s[i+j]
                    if starter not in current_word : 
                        current_word += starter
                        word_dict[current_word] = len(current_word)
                    else :
                        break
            return max(word_dict.values())
        else : return len(set(s))

s = 'pwwkew'
print(Solution().lengthOfLongestSubstring(s))