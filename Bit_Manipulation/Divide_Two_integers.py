class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negative = (dividend < 0) != (divisor < 0)

        dividend = -dividend if dividend < 0 else dividend
        divisor = -divisor if divisor < 0 else divisor

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            count = 1

            # Double the divisor until it is too large.
            while dividend >= (temp << 1):
                temp = temp << 1
                count = count << 1

            dividend = dividend - temp
            quotient = quotient + count

        if negative:
            quotient = -quotient

        return quotient


# Example:
# dividend = 10, divisor = 3
# Output: 3
