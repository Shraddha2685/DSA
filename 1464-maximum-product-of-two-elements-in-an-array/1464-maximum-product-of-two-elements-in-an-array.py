class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = (nums[-1]-1)*(nums[-2]-1)
        return result