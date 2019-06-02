from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        
        
        def could_palce(d,row,col):
            box = (row // 3) * 3 + col // 3
            return not (d in rows[row] or d in cols[col] or d in boxs[box] )
        
        
        
        def place_next_num(row,col):
            if row == 8 and col == 8:
                nonlocal shudu_solved
                shudu_solved = True
                 
            else:
                if col == 8:
                    backtrack(row+1,0)
                else:
                    backtrack(row, col + 1)
        
        def remove_num(d,row,col):
            del rows[row][d]
            del cols[col][d]
            box = (row // 3) * 3 + col // 3
            del boxs[box][d]
            board[row][col] = '.'
        
        def place_num(d,row,col):
            rows[row][d] +=1
            cols[col][d] += 1
            
            box_index = (row//3) *3 + col // 3
            boxs[box_index][d]  += 1
            
            board[row][col] = str(d)
        
        def backtrack(row=0,col = 0):
            if board[row][col] == '.':
                for d in range(1,10):
                    if could_palce(d,row,col):
                        place_num(d,row,col)
                        place_next_num(row,col)
                        if not shudu_solved:
                            remove_num(d,row,col)
            else:
                place_next_num(row,col)
        
        
                 
        n = 3
        
        rows = [ defaultdict(int) for i in range(9)]
        cols = [ defaultdict(int) for i in range(9)]
        boxs = [ defaultdict(int) for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    place_num(num,i,j)
        
        shudu_solved = False
        backtrack()
                    
                    
                    