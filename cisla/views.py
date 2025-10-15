from django.shortcuts import render
a=0
b=0
apar=""
bpar=""
def index(request):
    if request.method == "GET":
            vysledok = 0
    if request.method == "POST":
        a = (request.POST["cislo1"])
        b = (request.POST["cislo2"])
        
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
         


    return render(request, 'cisla/index.html', {"vysledok": vysledok, "apar":apar ,"bpar":bpar})