from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a Counter dictionary to count the frequency of each number
        count_d = Counter(nums)

        # Use heapq to get the k most common elements
        most_common = heapq.nlargest(k, count_d.items(), key=lambda x: x[1])

        # Extract the keys (numbers) from the most common elements
        return [num for num, count in most_common]


# Example usage
s = Solution()
print(s.topKFrequent([1, 2, 2, 3, 3, 3], 2))  # Output: [3, 2]
print(s.topKFrequent([7, 7], 1))  # Output: [7]
