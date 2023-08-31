from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        
        for idx, num in enumerate(nums):
            print(idx,num)
            complement = target - num
            if complement in numMap:
                return [numMap[complement], numMap[num]]
            numMap[num] = idx
            print(numMap)
        return []
            
s = Solution()
print(s.twoSum([3,3],6))
