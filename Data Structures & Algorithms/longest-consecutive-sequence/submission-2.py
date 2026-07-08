class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        start = set()
        max_counter=0

        for i in s:
            if (i-1) not in s:
                start.add(i)

        print(start)
        
        for i in start:
            counter=1
            while i+1 in s:
                print(i, end=" ")
                i += 1
                counter += 1
                print(counter)
            


            if counter>max_counter:
                max_counter=counter

        return max_counter