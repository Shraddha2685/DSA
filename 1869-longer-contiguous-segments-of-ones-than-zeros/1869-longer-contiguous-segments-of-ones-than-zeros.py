class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones = cur_ones = 0
        max_zeroes = cur_zeroes = 0
        
        for i in s:
            if i == "1":
                cur_ones += 1
                cur_zeroes = 0
            else:
                cur_zeroes += 1
                cur_ones = 0

            max_ones = max(max_ones, cur_ones)
            max_zeroes = max(max_zeroes, cur_zeroes)

        return max_ones > max_zeroes