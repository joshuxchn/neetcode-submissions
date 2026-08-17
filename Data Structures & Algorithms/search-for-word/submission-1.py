class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        def backtrack(row, col, i):
            nonlocal found
            #if global index == length of word, return true
            if i == len(word):
                found = True
                return
            #if out of the board, return
            if (row == len(board) or row < 0 or col < 0 or col == len(board[0])):
                return
            #if not the same char, return
            if board[row][col] != word[i]:
                return
                
            t = board[row][col]
            board[row][col] = "#" # mark as used
            backtrack(row - 1, col, i + 1)
            backtrack(row + 1, col, i + 1)
            backtrack(row, col + 1, i + 1)
            backtrack(row, col - 1, i + 1)
            #call the top,bottom,left,right
                #iterate global index

            board[row][col] = t
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    backtrack(row, col, 0)
        return found

            


            

        

        return char == len(word) - 1



#rules for word to exist
# 1) difference between two words is at max 1, for every consecutive word
#   ex: C is at (0, 2), A is at (1, 2), T is at (1, 3)