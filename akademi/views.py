from django.http import HttpResponse
from django.shortcuts import render
from .models import duvar_Kagidi
from .models import duvar_Paneli

data = {
    "duvar_kagidi": [
        {
            "image": "/duvar_kagitlari/27.jpg",
            "category": "duz",
            "price": "30",
            "title": "efsane"
        },
        {
            "image": "/duvar_kagitlari/60.jpg",
            "category": "damask",
            "price": "40",
            "title": "baya iyi"
        },
        {
            "image": "/duvar_kagitlari/103.jpg",
            "category": "cizgili",
            "price": "10",
            "title": "çok güzel"
        }
    ]
}

data2 = {
    "duvar_paneli": [
        {
            "image": "/duvar_panelleri/113.png",
            "price": "30",
            "title": "efsane"
        }, 
        {
            "image": "/duvar_panelleri/50.jpg",
            "price": "50",
            "title": "muhteşem"
        }
    ]
}

# Create your views here.
def index(request):
    return render(request, "index.html")

def duvar_kagidi(request):
    duvar_kagitlari = duvar_Kagidi.objects.all()
    context =  {
        "duvar_kagitlari": duvar_kagitlari
    }
    return render(request, "duvar_kagidi.html", context)

def duvar_paneli(request):
    duvar_panelleri = duvar_Paneli.objects.all()
    context =  {
        "duvar_panelleri": duvar_panelleri
    }
    return render(request, "duvar_paneli.html", context)

def stropiyer(request):
    return render(request, "stropiyer.html")

def tavan_kaplama(request):
    return render(request, "tavan_kaplama.html")

def citalama_dekor(request):
    return render(request, "citalama_dekor.html")

def iletisim(request):
    return render(request, "iletisim.html")