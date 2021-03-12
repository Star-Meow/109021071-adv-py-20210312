class hero:
    '''
    -------------------------
    15~20 defind name id amrror hp atk movespeed
    29~31 defind info
    32~34 print info what





    -------------------------
    '''
    def __init__(self, name, id, amrror, hp, atk, movespeed):
        self.heroname = name
        self.heroid = id
        self.heroamrror = amrror
        self.herohp = hp
        self.heroatk = atk
        self.heromovespeed =  movespeed
    def showinfo(self):
        print (self.heroname)
        print (self.heroamrror)
        print (self.herohp)
        print (self.heroatk)
        print (self.heromovespeed)


x = hero("Iana", "001", "一甲", "100", "35", "三速")
y = hero("kapkan", "002", "二甲", "100","28","二速")
z = hero("ash", "003", "一甲", "100","25","三速")
print(x.heroname, "\t", x.heroamrror, "\t", x.herohp, "\t", x.heroatk, "\t", x.heromovespeed)
print(y.heroname, "\t", y.heroamrror, "\t", y.herohp, "\t", y.heroatk, "\t", y.heromovespeed)
print(z.heroname, "\t", z.heroamrror, "\t", z.herohp, "\t", z.heroatk, "\t", z.heromovespeed)

x.showinfo()
y.showinfo()
z.showinfo()