class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        stack.append(0)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: #if in decreasing order
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        print(result)
        return result

             