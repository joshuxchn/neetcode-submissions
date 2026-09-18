class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #3
        #6
        #4
        prev = -1
        tally = len(speed)
        speed = [s for p, s in sorted(zip(position, speed), reverse=True)]
        position.sort(reverse=True)

        for i in range(len(speed)):
            time = (target-position[i])/speed[i]
            # print(time, stack)
            if prev != -1 and time <= prev:
                tally -= 1
                continue
            prev = time

        return tally
