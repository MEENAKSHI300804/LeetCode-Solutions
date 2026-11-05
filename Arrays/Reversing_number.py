class Solution(object):
    def reverse(self,x):
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        rev=int(str(x)[::-1])
        reverse=rev*sign
        if reverse<-2**31 or reverse>2**31-1:
            return 0
        return reverse
obj = Solution()

x = int(input("Enter a number: "))

result = obj.reverse(x)

print("Reversed number:", result)
