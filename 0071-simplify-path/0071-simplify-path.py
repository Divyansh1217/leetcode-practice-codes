class Solution:
    def simplifyPath(self, path: str) -> str:
        d = path.split('/')
        stack = []
        for i in d:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
        
        
        