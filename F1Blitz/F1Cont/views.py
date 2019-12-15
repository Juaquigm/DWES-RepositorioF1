from django.shortcuts import render
from .models import *

def lista_f1(request):
    pilotos = Piloto.objects.order_by('Nombre')
    return render(request, 'F1Cont/lista_F1.html', {'pilotos':pilotos})

# Create your views here.
