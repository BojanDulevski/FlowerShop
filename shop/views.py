from django.shortcuts import render, get_object_or_404
from .models import Buket

def site_buketi(request):
    buketi = Buket.objects.all()
    return render(request, 'shop/index.html', {'buketi': buketi})

def detali_buket(request, pk):
    buket = get_object_or_404(Buket, pk=pk)
    return render(request, 'shop/product.html', {'buket': buket})