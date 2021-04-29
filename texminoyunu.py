import random as r
tesadufibirreqem = r.randint(1,100)
print("*************Texmin etme oyunu**************")
print("reqemi 0-100 araliginda secin !")
while True:
    print("*****************")
    texmin = int(input("reqemi texmin edin:"))

    if texmin == tesadufibirreqem:
        print("*****************")
        for i in range(5):
            print("!!Tebrikler dogru reqemi tapdiniz!!")
        print("*****************")
        break
    elif texmin < tesadufibirreqem:
        print("*****************")
        print("Daha boyuk reqem yazin")
    elif texmin > tesadufibirreqem:
        print("*****************")
        print("Daha kicik reqem yazin")
