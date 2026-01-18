from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def index(request):
    products = Product.objects.all()
    return render(request , "shop/index.html",{"products":products})

def about(request):
    return HttpResponse("we are at about")
def contact(request):
    return HttpResponse("we are at contact us ")
def tracker (request):
    return HttpResponse("we are at tracker")
def search(request):
    return HttpResponse("we are at search")
def product_view(request):
    return HttpResponse("we are at product view")
def checkout(request):
    return HttpResponse("we are at checkout")