class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_i = Counter(nums)

        for i,count in count_i.items():
            if count == 1:
                return i

        return -1