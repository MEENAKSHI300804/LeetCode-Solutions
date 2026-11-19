class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        count=0
        for i in range(0,len(s)):
            if s[i] in " ":
                count=0
            else:
                count+=1
        return count