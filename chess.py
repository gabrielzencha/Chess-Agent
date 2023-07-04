import tkinter as tk

class ChessBoard:
    def __init__(self, rows=8, cols=8):
        self.window = tk.Tk()
        self.window.title("Chess")
        self.rows = rows
        self.cols = cols

        # Create the canvas and the chessboard
        self.canvas = tk.Canvas(self.window, width=800, height=800)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.draw_board)

        # Define the initial board positions
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

        self.window.mainloop()

    def draw_board(self, event=None):
        # Delete all current items on the canvas
        self.canvas.delete("all")

        # Get the new size of the canvas
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Calculate the size of each square
        square_width = width // self.cols
        square_height = height // self.rows

        # Draw the chessboard and pieces
        for row in range(self.rows):
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    color = 'white'
                else:
                    color = 'gray'
                self.canvas.create_rectangle(
                    col * square_width, row * square_height,
                    (col + 1) * square_width, (row + 1) * square_height,
                    fill=color
                )
                piece = self.board[row][col]
                if piece != ' ':
                    self.canvas.create_text(
                        col * square_width + square_width // 2,
                        row * square_height + square_height // 2,
                        text=piece,
                        font=("Arial", square_height // 2),
                        fill="black"
                    )

        self.canvas.bind("<Button-1>", self.square_clicked)

    def square_clicked(self, event):
        square_width = self.canvas.winfo_width() // self.cols
        square_height = self.canvas.winfo_height() // self.rows

        row = event.y // square_height
        col = event.x // square_width

        print(f"Square clicked: {row}, {col}")

if __name__ == "__main__":
    ChessBoard().draw_board()
