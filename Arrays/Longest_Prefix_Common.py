class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first=strs[0]
        last=strs[-1]
        count=0
        for i in range(min(len(first),len(last))):
            if first[i]==last[i]:
                count+=1
            else:
                break
        return first[:count]
        