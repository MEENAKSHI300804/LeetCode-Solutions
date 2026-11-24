class Solution(object):
    def isPalindrome(self, s):
        lowercase=s.lower()
        removing=re.sub(r'[^a-zA-Z0-9]', '', lowercase)#any chr that is not a letter or number.
        reverse=removing[::-1]
        if removing==reverse:
            return True
        else:
            return False