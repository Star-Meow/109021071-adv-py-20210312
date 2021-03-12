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
        print (hero.__dict__)
        print (hero.__doc__)
        print (hero.__name__)
        print (hero.__module__)
        print (hero.__base__)


x = hero("Iana", "001", "0", "100", "35", "35")
y = hero("kapkan", "002", "20", "100","28","40")
z = hero("ash", "003", "0", "100","25","80")
print(x.heroname, "\t", x.heroamrror, "\t", x.herohp, "\t", x.heroatk, "\t", x.heromovespeed)
print(y.heroname, "\t", y.heroamrror, "\t", y.herohp, "\t", y.heroatk, "\t", y.heromovespeed)
print(z.heroname, "\t", z.heroamrror, "\t", z.herohp, "\t", z.heroatk, "\t", z.heromovespeed)
