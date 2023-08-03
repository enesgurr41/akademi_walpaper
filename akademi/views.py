from django.http import HttpResponse
from django.shortcuts import render
from .models import duvar_Paneli
from .models import akadem1_Model
from .models import akadem2_Model
from .models import akadem3_Model
from .models import akadem4_Model
from .models import serisonu_Model
from .models import blog_Model
from .models import poster_Model
from .models import stropiyer_Model
from .models import aka_Kids
from .models import tavan_Kaplama
from .models import citalama_Dekor

# Create your views here.
def index(request):
    return render(request, "index.html")

def akadem1(request):
    akadem1_photo = akadem1_Model.objects.all()
    context =  {
        "akadem1_photo": akadem1_photo
    }
    return render(request, "akadem1.html", context)

def akadem2(request):
    akadem2_photo = akadem2_Model.objects.all()
    context =  {
        "akadem2_photo": akadem2_photo
    }
    return render(request, "akadem2.html", context)

def akadem3(request):
    akadem3_photo = akadem3_Model.objects.all()
    context =  {
        "akadem3_photo": akadem3_photo
    }
    return render(request, "akadem3.html", context)

def akadem4(request):
    akadem4_photo = akadem4_Model.objects.all()
    context =  {
        "akadem4_photo": akadem4_photo
    }
    return render(request, "akadem4.html", context)

def serisonu(request):
    serisonu_photo = serisonu_Model.objects.all()
    context =  {
        "serisonu_photo": serisonu_photo
    }
    return render(request, "serisonu.html", context)

def duvar_paneli(request):
    duvar_panelleri = duvar_Paneli.objects.all()
    context =  {
        "duvar_panelleri": duvar_panelleri
    }
    return render(request, "duvar_paneli.html", context)

def poster(request):
    poster_photo = poster_Model.objects.all()
    context =  {
        "poster_photo": poster_photo
    }
    return render(request, "poster.html", context)

def blog(request):
    blog_photo = blog_Model.objects.all()
    context =  {
        "blog_photo": blog_photo
    }
    return render(request, "blog.html", context)

def stropiyer(request):
    stropiyer_photo = stropiyer_Model.objects.all()
    context =  {
        "stropiyer_photo": stropiyer_photo
    }
    return render(request, "stropiyer.html", context)

def akakids(request):
    akakids_photo = aka_Kids.objects.all()
    context =  {
        "akakids_photo": akakids_photo
    }
    return render(request, "akakids.html", context)

def tavan_kaplama(request):
    tavankaplamalari = tavan_Kaplama.objects.all()
    context =  {
        "tavankaplamalari": tavankaplamalari
    }
    return render(request, "tavan_kaplama.html", context)

def citalama_dekor(request):
    citalamadekorlari = citalama_Dekor.objects.all()
    context =  {
    "citalamadekorlari": citalamadekorlari
    }
    return render(request, "citalama_dekor.html", context)

def iletisim(request):
    return render(request, "iletisim.html")