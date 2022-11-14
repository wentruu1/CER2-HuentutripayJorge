from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    return render(request, 'core/contacto.html')

def correspondencia(request):
    if request.method == 'POST':
        form = FiltrarResidencia(request.POST)
        if form.is_valid():
            residencia = form.cleaned_data["residencia"]
            correspondencias = Correspondencia.objects.filter(casa__exact=residencia)
    else:
        correspondencias = Correspondencia.objects.all()
        form = FiltrarResidencia()
    context = {'form': form, 'correspondencias':correspondencias}
    return render(request, 'core/correspondencia.html', context)
# Create your views here.

