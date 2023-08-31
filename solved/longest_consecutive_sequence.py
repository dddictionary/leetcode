from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0

        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                counter += 1
            else:
                counter = 0
            max_counter = max(counter, max_counter)
        return max_counter + 1
    


s = Solution()
print(s.longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive(nums=[100,4,200,1,3,2]))