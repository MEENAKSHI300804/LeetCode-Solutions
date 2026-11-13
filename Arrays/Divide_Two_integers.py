class Solution(object):
    def divide(self, dividend, divisor):
        MAX=2**31-1
        MIN=-2**31
        if dividend==MIN and divisor==-1:
            return MAX
        sign=1
        if dividend<0:
            sign=-sign
        if divisor<0:
            sign=-sign
        dividend=abs(dividend)
        divisor=abs(divisor)
        quotient=0
        while dividend>=divisor:
            temp=divisor
            count=1
            while dividend>=(temp<<1):
                temp=temp<<1
                count=count<<1
            dividend=dividend-temp
            quotient+=count
        if sign <0:
            quotient=-quotient

        return quotient