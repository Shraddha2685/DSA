class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count_i = Counter(nums)
        result = []
        for i, count in count_i.items():
            if count == 1:
                result.append(i)
        
        return result