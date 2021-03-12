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
        print (self.heroname,end="\t")
        print (self.heroamrror,end="\t")
        print (self.herohp,end="\t")
        print (self.heroatk,end="\t")
        print (self.heromovespeed,end="\t")



x = hero("Iana", "001", "一甲", "100", "35", "三速")
y = hero("kapkan", "002", "二甲", "100","28","二速")
z = hero("ash", "003", "一甲", "100","25","三速")


x.showinfo()
print(end="\n")
y.showinfo()
print(end="\n")
z.showinfo()