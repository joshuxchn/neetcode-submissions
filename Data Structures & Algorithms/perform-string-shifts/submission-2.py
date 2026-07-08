class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shift_total=0
        for pair in shift:
            if pair[0] == 0:
                shift_total -= pair[1]
            else:
                shift_total += pair[1]
        shift_total += len(s) * 10
        shift_total = shift_total % len(s)

        print(shift_total)
        right_side = s[len(s)-shift_total:len(s)]
        print(right_side)
        temp = s[0:len(s)-shift_total]
        print(temp)
        return right_side + temp