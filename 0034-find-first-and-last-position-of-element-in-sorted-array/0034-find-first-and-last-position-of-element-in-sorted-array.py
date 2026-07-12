class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        start = -1
        end =-1
        i=0
        j=n-1

        while(i<=j):
            if nums[i] == target:
                start = i
                break
            else:
                i += 1
            
        while(i<=j):
            if nums[j] == target:
                end = j
                break
            else:
                j -= 1

        return [start,end]