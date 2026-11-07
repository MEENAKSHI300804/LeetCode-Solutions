class Solution(object):
    def isValid(self, s):
        stack=[]
        brackets={']':'[',')':'(','}':'{'}
        for ch in s:
            if ch in brackets:
                if not stack:
                    return False
                if stack[-1]==brackets[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack)==0
