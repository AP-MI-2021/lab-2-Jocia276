def get_leap_years(start, end) :

    """
    Afiseaza toti anii bisecti intre doi ani dati(inclusiv anii dati)

     input : start, end -> int
     output : anii bisecti dintre start si end -> list[int]

     """
    list = []

    if start<end :
        print ("Anii bisecti intre " + str(start) + " si " + str(end) + " sunt: ")

    while start<=end :
         if (start % 4 == 0) and (start % 100 != 0) or (start % 100 ==0 ) and (start % 400 ==0) :
            list.append (int(start))
         start=start+1

    return list

start = int(input("Dati primul an: "))
end = int(input("Dati ultimul an: "))

print(get_leap_years(start, end))