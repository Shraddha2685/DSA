class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        store = []
        zeroes = []
        for i in nums:
            if i != 0:
                store.append(i)
            else:
                zeroes.append(i)

        nums[:] = store + zeroes