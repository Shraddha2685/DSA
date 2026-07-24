class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        for i in nums:
            freq[i] = freq.get(i,0)+1

        for i in nums:
            if freq[i] > 1 and i not in result:
                result.append(i)

        result.sort()
        return result