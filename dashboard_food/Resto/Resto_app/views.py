from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    Rest = Resto_list.objects.all()
    return render(request, 'restaurant list.html')


def product(request):
    # text = request.POST['date']
    # value = text+"hi"
    return render(request, 'restoReg.html')


def successDB(request):
    Name = request.POST['name']
    Review = request.POST['review']
    sale = request.POST['sale']
    date = request.POST['date']
    status = request.POST['status']
    Rest = Resto_list.objects.create(
        Name=Name, Review=Review, sale=sale, date=date, status=status)
    Rest.save()
    # a1 = Rest.sale
    return render(request, 'successDB.html', {'val': Name})
