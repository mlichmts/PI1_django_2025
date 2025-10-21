from django.shortcuts import render
a=0
b=0


def index(request):

    apar = ""
    bpar = ""
    vysledok_prvocislo=""
    vysledok_prvocislob=""


    if request.method == "GET":
            vysledok = 0
    if request.method == "POST":
        a = int((request.POST["cislo1"]))
        b = int((request.POST["cislo2"]))
        
        if a>b:
             vysledok="cislo a je vacsie"
        elif b>a:
             vysledok ="cislo b je vacsie"  
        else:
             vysledok ="cisla su rovnake"              
    
             
        if a%2 == 0:
            apar = "cislo A je parne"

        else:
            apar = "cislo A je neparne"
             
        if b%2 == 0:
            bpar = "cislo B je parne"

        else:
            bpar = "cislo B je neparne"
         
        if a <= 1:
            prvocislo = False
        else:
            prvocislo = True
            for i in range(2, a):
                if a % i == 0:
                    prvocislo = False
                    break

        if prvocislo:
            vysledok_prvocislo = "cislo a je prvočíslo"
        else:
            vysledok_prvocislo = "cislo a nie je prvočíslo"


        if b <= 1:
            prvocislob = False
        else:
            prvocislob = True
            for i in range(2, b):
                if b % i == 0:
                    prvocislob = False
                    break

        if prvocislob:
            vysledok_prvocislob = "cislo b je prvočíslo"
        else:
            vysledok_prvocislob = "cislo b nie je prvočíslo"

    return render(request, 'cisla/index.html', {"vysledok": vysledok,"apar": apar,"bpar": bpar,"vysledok_prvocislo":vysledok_prvocislo,"vysledok_prvocislob":vysledok_prvocislob})