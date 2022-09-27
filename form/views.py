from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Kota,Form
from django.contrib import messages

# Create your views here.
def index(request):
    k = Kota.objects.all()
    context = {
        'title': 'Pengajuan Kredit',
        'header': 'Pengajuan Kredit',
        'kota': k,
    }
    return render(request, 'form/index.html',context)

def modal(request):
    context = {
        'title': 'Success'
    }
    return render(request, 'form/modal.html',context)

def addform(request):
    if request.method == "POST":
        pinjaman = request.POST['pinjaman']
        tenor = request.POST['tenor']
        angsuran = request.POST['angsuran']
        nama = request.POST['nama']
        telp = request.POST['telp']
        email = request.POST['email']
        alamat = request.POST['alamat']
        f = Form(pinjaman=pinjaman,tenor=tenor,angsuran=angsuran,nama=nama,telp=telp,email=email,alamat=alamat,kota_id=Kota.objects.get(id=request.POST['kota']))
        f.save()
        messages.success(request, "Berhasil Memperbaharui Data Divisi")
    else:
        pass
    return redirect(modal)