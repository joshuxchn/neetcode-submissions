class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row in range(len(words)):
            for column in range(len(words[row])):
                print(row, column)
                if column >= len(words) or row >= len(words[column]):
                    return False
                if words[row][column] != words[column][row]:
                    return False


        return True