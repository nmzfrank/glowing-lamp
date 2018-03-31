import tkinter


class PW():
    """used for quickly draw physic widgets"""

    def __init__(self, arg):
        self.arg = arg
        self.root = tkinter.Tk()
        self.cv = tkinter.Canvas(self.root, bg='white')
        self.item_list = []
        self.bg_list = []
        self.link_list = []

    def __calc_attach(self):
        pass

    def add_static_block(self, tag, attach='attach', coords=[], on=None, pos_x=-1, pos_y=-1):
        if attach == 'attach':
            if on is not None:
                item = self.cv.create_polygon(coords, fill='red')
                self.cv.addtag_withtag(tag, item)
                self.item_list.append(item)
        else:
            item = self.cv.create_polygon(coords, fill='red')
            self.cv.addtag_withtag(tag, item)
            self.item_list.append(item)

    def add_static_ball(self, tag, attach='attach', to=None, coords=[]):
        if attach == 'attach':
            if to is not None:
                item = self.cv.create_oval(coords[0][0], coords[0][1], coords[1][0], coords[1][1])
                self.cv.addtag_withtag(tag, item)
                self.item_list.append(item)
        else:
            item = self.cv.create_oval(coords[0][0], coords[0][1], coords[1][0], coords[1][1])
            self.cv.addtag_withtag(tag, item)
            self.item_list.append(item)

    def add_flat(self, tag, attach='attach', connect=None, coords=[], shadow=False):
        if attach == 'attach':
            if connect is not None:
                item = self.cv.create_line(coords)
                self.cv.addtag_withtag(tag, item)
                self.bg_list.append(item)
        else:
            item = self.cv.create_line(coords)
            self.cv.addtag_withtag(tag, item)
            self.bg_list.append(item)

    def add_ramp(self, tag, attach='attach', connect=None, slope=0, coords=[], shadow=False):
        # slope refer to degree
        if attach == 'attach':
            if connect is not None:
                item = self.cv.create_line(coords)
                self.cv.addtag_withtag(tag, item)
                self.bg_list.append(item)
        else:
            item = self.cv.create_line(coords)
            self.cv.addtag_withtag(tag, item)
            self.bg_list.append(item)

    def show(self):
        self.cv.pack()
        self.root.mainloop()


if __name__ == '__main__':
    pw = PW(111)
    pw.add_static_block('A', attach='manual', coords=[(1, 1), (1, 50), (50, 50), (50, 1)])
    pw.show()
