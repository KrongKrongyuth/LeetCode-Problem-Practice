class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) != 0 :
            if s.isalpha() and len(s) > 1 :
                current_word, word_dict = "", {}
                for i in range(len(s)) :
                    current_word = ""
                    for j in range(len(s[i:])) :
                        starter = s[i+j]
                        print(starter, i, j, i+j)
                        if starter not in current_word : 
                            current_word += starter
                            word_dict[current_word] = len(current_word)
                        else :
                            break
                print(word_dict)
                return max(word_dict.values())
            else : return len(set(s))
        else : return 0

s = 'pwwkew'
print(Solution().lengthOfLongestSubstring(s))