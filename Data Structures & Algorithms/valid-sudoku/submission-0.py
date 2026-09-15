class Solution:
    def isValidRow(self, row: List[str]) -> bool:
        visited = set()
        for c in row: 
            if c != '.':
                if c in visited:
                    return False
                else:
                    visited.add(c)
        return True


    def isValidColumn(self, board: List[List[str]], column: int) -> bool:
        visited = set()
        for row in board:
            if row[column] != '.':
                if row[column] in visited:
                    return False 
                else: 
                    visited.add(row[column])
        return True
                

    def isValidGrid(self, board: List[List[str]], corner: (int,int)) -> bool:
        visited = set()
        for i in range(3):
            for j in range(3): 
                c = board[corner[0]+i][corner[1]+j]
                if c != '.':
                    if c in visited:
                        return False
                    else:
                        visited.add(c)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidRow(row):
                return False
        
        for i in range(9):
            if not self.isValidColumn(board, i):
                return False
        
        for i in range(3):
            for j in range(3):
                if not self.isValidGrid(board, (i*3, j*3)):
                    return False
        
        return True


