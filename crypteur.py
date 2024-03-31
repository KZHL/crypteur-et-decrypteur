xx = input("Entrez le texte à crypter : ")
xxx = True
mot = ""

while xxx == True:
    for lettre in xx:
        if lettre == "a":
            mot += "b"
        elif lettre == "b":
            mot += "c"
        elif lettre == "c":
            mot += "d"
        elif lettre == "d":
            mot += "e"
        elif lettre == "e":
            mot += "f"
        elif lettre == "f":
            mot += "g"
        elif lettre == "g":
            mot += "h"
        elif lettre == "h":
            mot += "i"
        elif lettre == "i":
            mot += "j"
        elif lettre == "j":
            mot += "k"
        elif lettre == "k":
            mot += "l"
        elif lettre == "l":
            mot += "m"
        elif lettre == "m":
            mot += "n"
        elif lettre == "n":
            mot += "o"
        elif lettre == "o":
            mot += "p"
        elif lettre == "p":
            mot += "q"
        elif lettre == "q":
            mot += "r"
        elif lettre == "r":
            mot += "s"
        elif lettre == "s":
            mot += "t"
        elif lettre == "t":
            mot += "u"
        elif lettre == "u":
            mot += "v"
        elif lettre == "v":
            mot += "w"
        elif lettre == "w":
            mot += "x"
        elif lettre == "x":
            mot += "y"
        elif lettre == "y":
            mot += "z"
        elif lettre == "z":
            mot += "a"
        else:
            mot += lettre  
    print("Texte crypté :", mot)
    xxx = False
