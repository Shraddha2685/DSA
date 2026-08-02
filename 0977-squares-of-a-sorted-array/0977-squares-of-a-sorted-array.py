class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        result = []

        for i in nums:
            i = abs(i)*abs(i)
            result.append(i)
            
        result.sort()

        return result