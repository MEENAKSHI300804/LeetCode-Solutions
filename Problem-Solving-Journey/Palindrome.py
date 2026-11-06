class Solution(object):
    def isPalindrome(self, x):
        self.x=x
        return self.calculations()
    def calculations(self):
        reverse=0
        original=self.x
       #if self.x<0:
            #sign=-1
           #else:
            #sign=1
        while self.x>0:
            last_digit=self.x%10
            reverse=reverse*10+last_digit
            self.x=self.x//10
        if original<0:
            reverse=-reverse
        if original==reverse:
            return True
        else:
           return False