class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')


        stack = []
        for d in path:
            if len(d) != 0:
                stack.append(d)

                if d == '..':
                    stack.pop()
                    if stack:
                        stack.pop()
                elif d=='.':
                    stack.pop()
            print(stack)

        return '/' + "/".join(stack)