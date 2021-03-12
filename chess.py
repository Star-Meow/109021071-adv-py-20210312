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
        self.chessstep =  step
    def showinfo(self):
        print (self.chessname)
        print (self.chesscolor)
        print (self.chesscolumn)
        print (self.chessrow)
        print (self.chessstep)

x = hero("Iana", "001", "0", "100", "35", "35")
y = hero("kapkan", "002", "20", "100","28","40")
z = hero("ash", "003", "0", "100","25","80")
print(x.heroname, "\t", x.heroamrror, "\t", x.herohp, "\t", x.heroatk, "\t", x.heromovespeed)
print(y.heroname, "\t", y.heroamrror, "\t", y.herohp, "\t", y.heroatk, "\t", y.heromovespeed)
print(z.heroname, "\t", z.heroamrror, "\t", z.herohp, "\t", z.heroatk, "\t", z.heromovespeed)

showinfo