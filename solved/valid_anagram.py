from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        l = defaultdict(int)

        for letter in s:
            l[letter] += 1

        for letter in t:
            l[letter] -= 1
        
        for letters in l.values():
            if letters != 0: 
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)