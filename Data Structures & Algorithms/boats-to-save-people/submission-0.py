class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # two pointers: one start, one end
        # if start == limit, tally++
        # iterate start
        # else, compare the pointer combo, if match limit add in
        # 0, 0, 1, 2, 4, 5
        # 1, 2, 2, 3, 3
        people.sort()

        l = 0
        r = len(people) - 1
        tally = 0
        while l < r:
            if people[l] + people[r] <= limit:
                tally += 1
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                tally += 1
                r -= 1
            if l == r:
                tally += 1
        return tally
