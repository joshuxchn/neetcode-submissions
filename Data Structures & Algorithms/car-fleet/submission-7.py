class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #3
        #6
        #4
        stack = []
        speed = [s for p, s in sorted(zip(position, speed), reverse=True)]
        position.sort(reverse=True)

        for i in range(len(speed)):
            time = (target-position[i])/speed[i]
            # print(time, stack)
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)
