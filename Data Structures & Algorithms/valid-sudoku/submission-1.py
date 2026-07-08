class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            x = i // 3
            y = i % 3
            if not self.solveGrid(board, 3*x, 3*y):
                return False

        return self.solveColumn(board) 
    def solveGrid(self, board, topleftx, toplefty) -> bool:
        seen = set()
        for i in range(3):
            for z in range(3):
                val = board[topleftx + i][toplefty+z]
                if val == ".":
                    continue
                elif val in seen:
                    return False
                else:
                    seen.add(val)
        return True

    def solveColumn(self, board) -> bool:
        xsets = [set() for _ in range(9)]
        # ysets = [set() for _ in range(9)]

        for x in range(9):
            ysets = set()
            for y in range(9):
                val = board[x][y]
                if val == ".":
                    continue

                if val in ysets:
                    return False
                else:
                    ysets.add(val)
                
                if val in xsets[y]:
                    return False
                else:
                    xsets[y].add(val)
        
        return True

            
