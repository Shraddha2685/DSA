class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = sorted(list(set(nums)))
        if len(unique) <3:
            return unique[-1]

        return unique[-3]