import random

class Sudoku:
    def __init__(self):
        self.board = [[0]*9 for _ in range(9)]

    def is_valid(self, r, c, n):
        for i in range(9):
            if self.board[r][i] == n or self.board[i][c] == n:
                return False
        sr, sc = (r//3)*3, (c//3)*3
        for i in range(3):
            for j in range(3):
                if self.board[sr+i][sc+j] == n:
                    return False
        return True

    def solve(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    for n in range(1,10):
                        if self.is_valid(r,c,n):
                            self.board[r][c] = n
                            if self.solve():
                                return True
                            self.board[r][c] = 0
                    return False
        return True

    def fill_box(self, r, c):
        nums = list(range(1,10))
        random.shuffle(nums)
        k = 0
        for i in range(3):
            for j in range(3):
                self.board[r+i][c+j] = nums[k]
                k += 1

    def remove_cells(self, count=40):
        while count > 0:
            r = random.randint(0,8)
            c = random.randint(0,8)
            if self.board[r][c] != 0:
                self.board[r][c] = 0
                count -= 1

    def generate(self):
        for i in range(0,9,3):
            self.fill_box(i,i)
        self.solve()
        self.remove_cells()
