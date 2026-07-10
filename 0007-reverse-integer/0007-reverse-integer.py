class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        temp = abs(x)
        rev= 0
        while (temp>0):
            dig = temp%10
            rev = rev*10 + dig
            temp = temp // 10
        result = sign*rev

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result