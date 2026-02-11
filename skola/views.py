from django.shortcuts import render
from .models import Student,Ucitel
def index(request):
    studenti = Student.objects.all()
    return render(request, 'skola/index.html',{"studenti":studenti})