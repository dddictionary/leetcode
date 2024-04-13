from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for idx, num in enumerate(nums):
            ans.append(self.get_product(nums.remove(num)))
        return ans

    def get_product(self, nums):
        prod = 0
        for num in nums:
            prod *= num
        return prod