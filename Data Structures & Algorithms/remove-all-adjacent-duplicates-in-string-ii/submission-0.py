class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and char == stack[-1][0]:
                stack.append((char, stack[-1][1] + 1))
            else:
                stack.append((char, 1))

            if stack[-1][1] == k:
                for a in range(k):
                    stack.pop()

        return "".join(item[0] for item in stack)