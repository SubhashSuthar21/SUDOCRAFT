from flask import Flask, render_template, request, jsonify
from sudoku_cli import Sudoku

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/generate")
def generate():
    s = Sudoku()
    s.generate()
    return jsonify({"board": s.board})

@app.route("/api/solve", methods=["POST"])
def solve_api():
    board = request.json["board"]
    solve(board)
    return jsonify({"solution": board})

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1,10):
                    if valid(board,i,j,n):
                        board[i][j] = n
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def valid(board,r,c,n):
    for i in range(9):
        if board[r][i] == n or board[i][c] == n:
            return False
    sr, sc = (r//3)*3, (c//3)*3
    for i in range(3):
        for j in range(3):
            if board[sr+i][sc+j] == n:
                return False
    return True

if __name__ == "__main__":
    app.run(debug=True)
