
def teza_ladje(teza):
    stevec = 0
    teza_goriva = 0
    while teza > 0:
        teza = (teza // 3) - 2
        teza_goriva += teza
        stevec += 1
        #print(stevec, teza, teza_goriva)

    print("Za prevoz vaseg tovora potrebujete", stevec, "ton goriva i dodatnih", int(teza_goriva), "ton goriva.")

teza_ladje(float(input("Unesite tezo tovara ladje: ")))