# 三角形・四角形
# coding:utf-8
import tkinter as tk
class Ball:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def move(self, canvas):
        # いまの円を消す
        self.erase(canvas)
        # X座標、Y座標を動かす
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        # 次の位置に円を描画する
        self.draw(canvas)
        # 端を超えていたら反対向きにする
        if (self.x >= canvas.winfo_width()):
            self.dx = -3
        if (self.x <= 0):
            self.dx = 3
        if (self.y >= canvas.winfo_height()): 
            self.dy = -3
        if (self.y <= 0):
            self.dy = 3

    def erase(self, canvas):
        canvas.create_oval(self.x -20, self.y -20, self.x +20, self.y + 20, fill="white", width=0)
    def draw(self, canvas):
        canvas.create_oval(self.x -20, self.y -20, self.x +20, self.y +20, fill=self.color, width=0)

class Rectangle(Ball):
    def erase(self, canvas):
        canvas.create_rectangle(self.x -20, self.y -20, self.x +20, self.y + 20, fill="white", width=0)
    def draw(self, canvas):
        canvas.create_rectangle(self.x -20, self.y -20, self.x +20, self.y +20, fill=self.color, width=0)
    def move(self, canvas):
        # いまの円を消す
        self.erase(canvas)
        # X座標、Y座標を動かす
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        # 次の位置に円を描画する
        self.draw(canvas)
        # 端を超えていたら反対向きにする
        if (self.x >= canvas.winfo_width()):
            self.dx = -9
        if (self.x <= 0):
            self.dx = 9
        if (self.y >= canvas.winfo_height()): 
            self.dy = -9
        if (self.y <= 0):
            self.dy = 9

class Triangle(Ball):
    def erase(self, canvas):
        canvas.create_polygon(self.x, self.y -20, self.x +20, self.y + 20, self.x -20, self.y +20, fill="white", width=0)
    def draw(self, canvas):
        canvas.create_polygon(self.x, self.y -20, self.x +20, self.y + 20, self.x -20, self.y +20, fill=self.color, width=0)


# 円を複数作る
balls = [
    Ball(400, 300, 1, 1, "red"),
    Rectangle(200, 100, -1, 1, "green"),
    Triangle(100, 200, 1, -1, "blue")
]

def loop():
    # 動かす
    for b in balls:
        b.move(canvas)
    # もう一回
    root.after(10,loop)

# ウィンドウを描く
root = tk.Tk()
root.geometry("800x600")

# Canvasを置く
canvas =tk.Canvas(root, width =800, height =600, bg="#fff")
canvas.place(x = 0, y = 0)

# タイマーをセット
root.after(10, loop)

root.mainloop()