class chess:
    '''
    -------------------------



    -------------------------
    '''
    def __init__(self, name, color, column, row, step):
        self.chessname = name
        self.chesscolor = color
        self.chesscolumn = column
        self.chessrow = row
        self.chessstep = step
    def showinfo(self):
        print (self.chessname,end="\t")
        print (self.chesscolor,end="\t")
        print (self.chesscolumn,end="\t")
        print (self.chessrow,end="\t")
        print (self.chessstep,end="\t")

a = chess("將", "黑", "7", "13", "2")
b = chess("帥", "紅", "7", "1", "1")
c = chess("卒", "黑", "7", "6", "1")
d = chess("兵", "紅", "7", "5", "1")


a.showinfo()
print(end="\n")
b.showinfo()
print(end="\n")
c.showinfo()
print(end="\n")
d.showinfo()