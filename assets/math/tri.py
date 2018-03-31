import tkinter
import math


def draw_normal_axis(canvas):
    canvas.create_line(400, 0, 400, 400, fill="red", tags="y_axis")
    canvas.create_line(400, 0, 395, 10, fill="red", tags="y_axis")
    canvas.create_line(400, 0, 405, 10, fill="red", tags="y_axis")
    canvas.create_line(0, 200, 800, 200, fill="red", tags="x_axis")
    canvas.create_line(800, 200, 790, 195, fill="red", tags="x_axis")
    canvas.create_line(800, 200, 790, 205, fill="red", tags="x_axis")
    for i in range(15):
        canvas.create_line((i + 1) * 50, 200, (i + 1) * 50, 195, fill="red", tags="x_axis")
        if i == 7:
            canvas.create_text(405, 208, text='0')
        else:
            canvas.create_text((i + 1) * 50, 208, text=str(i - 7))
    for j in range(7):
        canvas.create_line(400, (j + 1) * 50, 405, (j + 1) * 50, fill="red", tags="y_axis")
        if j == 3:
            continue
        canvas.create_text(412, (j + 1) * 50, text=str(3 - j))


def draw_tri_axis(canvas):
    axis_name = ['-7/2π', '-3π', '-5/2π', '-2π', '-3/2π', '-π', '-1/2π', '0', '1/2π', 'π', '3/2π', '2π', '5/2π', '3π', '7/2π']
    canvas.create_line(400, 100, 405, 100, fill="red", tags="y_axis")
    canvas.create_text(412, 100, text='1')
    canvas.create_line(400, 300, 405, 300, fill="red", tags="y_axis")
    canvas.create_text(412, 300, text='-1')
    for i in range(15):
        canvas.create_line((i + 1) * 50, 200, (i + 1) * 50, 195, fill="red", tags="x_axis")
        if i == 7:
            canvas.create_text(405, 208, text='0')
            continue
        canvas.create_text((i + 1) * 50, 208, text=axis_name[i])


def hello():
    print("hello")


def draw_new_func(top, canvas, A, w, phi, b):
    curve_coords = []
    for i in range(40, 760, 1):
        x = (i - 400) / 100 * math.pi
        y = 200 - (A * math.sin(x * w + phi) + b) * 100
        curve_coords.append((i, y))
    for i, coord in enumerate(curve_coords):
        if i == 0:
            continue
        canvas.create_line(curve_coords[i][0], curve_coords[i][1], curve_coords[i - 1][0], curve_coords[i - 1][1], width=2, fill='green')
    top.destroy()


def add_func(root, canvas):
    top = tkinter.Toplevel(root)
    A = tkinter.Entry(top)
    w = tkinter.Entry(top)
    phi = tkinter.Entry(top)
    b = tkinter.Entry(top)
    tkinter.Label(top, text="A: ").grid(row=0)
    A.grid(row=0, column=1, padx=5, pady=10)
    tkinter.Label(top, text="w: ").grid(row=1)
    w.grid(row=1, column=1, padx=5, pady=10)
    tkinter.Label(top, text="φ: ").grid(row=2)
    phi.grid(row=2, column=1, padx=5, pady=10)
    tkinter.Label(top, text="b: ").grid(row=3)
    b.grid(row=3, column=1, padx=5, pady=10)
    confirm = tkinter.Button(top, text="OK", command=lambda: draw_new_func(top, canvas, float(A.get()), float(w.get()), float(phi.get()), float(b.get())))
    confirm.grid(row=4, columnspan=2)


def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, bg='white', width=800, height=400)
    canvas.create_line(400, 0, 400, 400, fill="red", tags="y_axis")
    canvas.create_line(400, 0, 395, 10, fill="red", tags="y_axis")
    canvas.create_line(400, 0, 405, 10, fill="red", tags="y_axis")
    canvas.create_line(0, 200, 800, 200, fill="red", tags="x_axis")
    canvas.create_line(800, 200, 790, 195, fill="red", tags="x_axis")
    canvas.create_line(800, 200, 790, 205, fill="red", tags="x_axis")
    # draw_tri_axis(canvas)
    # curve_coords = []
    # for i in range(40, 760, 1):
    #     x = (i - 400) / 100 * math.pi
    #     y = 200 - math.sin(x) * 100
    #     curve_coords.append((i, y))
    # # print(curve_coords)
    # for i, coord in enumerate(curve_coords):
    #     if i == 0:
    #         continue
    #     canvas.create_line(curve_coords[i][0], curve_coords[i][1], curve_coords[i - 1][0], curve_coords[i - 1][1], width=2)
    #     # print(curve_coords[i][0], curve_coords[i][1], curve_coords[i - 1][0], curve_coords[i - 1][1])
    # canvas.pack()
    # menubar = tkinter.Menu(root, tearoff=0)
    # menubar.add_command(label="add new function", command=lambda: add_func(root, canvas))
    # canvas.bind("<Button-3>", lambda event: menubar.post(event.x_root, event.y_root))
    draw_normal_axis(canvas)
    canvas.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
