from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        l = []
        for num in nums:
            m[num] += 1
        return sorted(m, key=m.get, reverse=True)[:k]
        