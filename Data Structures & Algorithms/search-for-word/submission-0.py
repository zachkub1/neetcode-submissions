class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def back(r,c,i):
            if i == len(word):
                return True
            
            if (r <0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != word[i]):
                return False
            
            #
            state, board[r][c] = board[r][c], '#'
            match = (back(r+1,c,i+1) or
            back(r-1,c,i+1)or
            back(r,c+1,i+1)or
            back(r,c-1,i+1))
            board[r][c]= state
            return match
        return any(back(r,c,0) for r in range(rows) for c in range(cols))