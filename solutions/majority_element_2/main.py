from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        th = length // 3
        rank = {k:0 for k in set(nums)}
        result = set()
        for e in nums:
            rank[e] += 1
            print(rank[e],e)
            if rank[e] > th:
                result.add(e)
        print(list(result))
        return list(result)
    
Solution().majorityElement([3,2,3])
            