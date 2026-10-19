class Solution(object):
    def divide(self, dividend, divisor):
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp += temp
                multiple += multiple

            dividend -= temp
            count += multiple

        result = -count if sign < 0 else count

        return min(max(result, -2147483648), 2147483647)