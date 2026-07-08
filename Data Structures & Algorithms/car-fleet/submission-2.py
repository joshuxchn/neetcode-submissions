class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        speed = [s for p, s in sorted(zip(position, speed), reverse=True)]
        position.sort(reverse=True)

        stack = []
        for i in range(len(position)):
            time = (target-position[i]) / speed[i]
            if not stack:
                stack.append(time)
                continue

            if time <= stack[-1]:
                continue
            else:
                stack.append(time)



        
        return len(stack)