class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')


        stack = []
        for d in path:
                
            if d == '..':
                if stack:
                    stack.pop()
            elif len(d) != 0 and d!='.':
                stack.append(d)

        return '/' + "/".join(stack)