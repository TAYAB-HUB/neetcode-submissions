class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [[False]*9 for _ in range(9)]
        c = [[False]*9 for _ in range(9)]
        b = [[False]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if(board[i][j]!="."):
                    n = ord(board[i][j])-ord("1")
                    bi = (i//3)*3+j//3
                    if r[i][n] or c[j][n] or b[bi][n]:
                        return False
                    r[i][n] = c[j][n] = b[bi][n] = True
        return True
        