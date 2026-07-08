class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0: #collision
                if abs(a) > stack[-1]:
                    stack.pop(-1) #negative destroyed positive
                    continue
                elif abs(a) == stack[-1]:
                    stack.pop() #a is destroyed, top is too
                break
                
            else:
                stack.append(a)
        
        return stack

            