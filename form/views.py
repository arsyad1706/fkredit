from django.shortcuts import render
from .models import Kota,Form

# Create your views here.
def index(request):
    k = Kota.objects.all()
    context = {
        'title': 'Pengajuan Kredit',
        'header': 'Pengajuan Kredit',
        'kota': k,
    }
    return render(request, 'form/index.html',context)