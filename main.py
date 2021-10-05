def main ():
    while True:
        print("1. Ani bisecti.")
        print("2. Patrate perfecte.")
        print("x. Iesire din program - exit.")
        optiune = input ("Alege optiunea: ")
        if optiune == "1":
            def get_leap_years(start, end):

                """
                Afiseaza toti anii bisecti intre doi ani dati(inclusiv anii dati)

                 input : start, end -> int
                 output : anii bisecti dintre start si end -> list[int]

                 """
                list = []

                if start < end:
                    print("Anii bisecti intre " + str(start) + " si " + str(end) + " sunt: ")

                while start <= end:
                    if (start % 4 == 0) and (start % 100 != 0) or (start % 100 == 0) and (start % 400 == 0):
                        list.append(int(start))
                    start = start + 1

                return list

            start = int(input("Dati primul an: "))
            end = int(input("Dati ultimul an: "))

            print(get_leap_years(start, end))
        elif optiune == "2":
            def get_perfect_squares(start, end):

                """
                  Afiseaza toate patratele perfecte intr-un interval inchis dat.

                    input : start, end -> int
                    output : numerele patrate perfecte intr start si end -> list[int]

                """

                list = []
                for i in range (start, end+1):
                    j=1
                    while j*j <= i:
                        if j*j == i:
                            list.append (i)
                        j=j+1
                    i=i+1
                return list

            start = int(input("Introduceti primul numar: "))
            end = int(input("Introduceti al doilea numar: "))

            print(get_perfect_squares(start, end))

        else :
            if optiune == "x":
                break
main()