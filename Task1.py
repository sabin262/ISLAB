class One:
    def Task1():
        x=input(">First Name: ").lower()
        y=input(">Last Name: ").lower()
        z=input(">Year of birth: ")
        print(x + " " + y + " " + z)
        snip=x[0]
        lsnip=y[0:6]
        ysnip=z[2:4]
        print(snip + lsnip + ysnip)
    Task1()
