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
                
            else: #if loop doesn't break, this is true. so while the negative is bigger
            #the loop destroys it. while the left positive is bigger, the loop just stops 
            # (because there is nothing there yet to destroy, we're calculating the negative direction, not the positve side.)
            # and that just means we destroyed "a", so we break and dont go the else append logic
                stack.append(a)
        
        return stack

            