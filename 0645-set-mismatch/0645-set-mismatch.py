class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)

        duplicate = -1
        missing = -1

        for i in range(1,n+1):
            if count[i] == 2:
                duplicate = i

            elif count[i] == 0:
                missing = i

        return [duplicate, missing]