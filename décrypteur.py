xx = input("Entrez le texte à décrypter : ")
xxx = True
mot = ""

while xxx == True:
    for lettre in xx:
        if lettre == "b":
            mot += "a"
        elif lettre == "c":
            mot += "b"
        elif lettre == "d":
            mot += "c"
        elif lettre == "e":
            mot += "d"
        elif lettre == "f":
            mot += "e"
        elif lettre == "g":
            mot += "f"
        elif lettre == "h":
            mot += "g"
        elif lettre == "i":
            mot += "h"
        elif lettre == "j":
            mot += "i"
        elif lettre == "k":
            mot += "j"
        elif lettre == "l":
            mot += "k"
        elif lettre == "m":
            mot += "l"
        elif lettre == "n":
            mot += "m"
        elif lettre == "o":
            mot += "n"
        elif lettre == "p":
            mot += "o"
        elif lettre == "q":
            mot += "p"
        elif lettre == "r":
            mot += "q"
        elif lettre == "s":
            mot += "r"
        elif lettre == "t":
            mot += "s"
        elif lettre == "u":
            mot += "t"
        elif lettre == "v":
            mot += "u"
        elif lettre == "w":
            mot += "v"
        elif lettre == "x":
            mot += "w"
        elif lettre == "y":
            mot += "x"
        elif lettre == "z":
            mot += "y"
        elif lettre == "a":
            mot += "z"
        else:
            mot += lettre  
    print("Texte décrypté :", mot)
    xxx = False
