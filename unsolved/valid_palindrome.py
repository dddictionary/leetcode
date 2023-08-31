from typing import List

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for c in s.lower():
            if c.isalpha():
                new_str += c

        # print(f"{new_str=}")
        if new_str == "":
            return True
        
        return new_str == str(reversed(new_str))
    

s = Solution()
# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
print(s.isPalindrome("aa"))