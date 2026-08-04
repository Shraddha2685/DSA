class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = min(nums)
        largest = max(nums)
        seen = set(nums)
        result = []

        for i in range(smallest, largest + 1):
            if i not in seen:
                result.append(i)

        return result