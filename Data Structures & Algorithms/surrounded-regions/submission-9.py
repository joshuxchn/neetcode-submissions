class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def valid(row, col):
            if min(row, col) < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != 'O':
                return False
            return True

        def dfs(row, col):

            board[row][col] = 'T'
            if valid(row+1, col): dfs(row + 1, col)
            if valid(row-1, col): dfs(row - 1, col)
            if valid(row, col+1): dfs(row, col + 1)
            if valid(row, col-1): dfs(row, col - 1)
        

        #mark all the edge ones first
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' and (min(row, col) == 0 or row == len(board) - 1 or col == len(board[0]) - 1):
                    dfs(row,col)

        #mark the inside, #unmark T's
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O' 
 
