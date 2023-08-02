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

data1 = {
    "akadem1": [
        {
            "image": "/akadem1_photo/27.jpg",
            "category": "duz",
            "price": "79",
            "title": "efsane"
        },
        {
            "image": "/akadem1_photo/60.jpg",
            "category": "damask",
            "price": "50",
            "title": "baya iyi"
        },
        {
            "image": "/akadem1_photo/103.jpg",
            "category": "cizgili",
            "price": "80",
            "title": "çok güzel"
        }
    ]
}

data2 = {
    "akadem2": [
        {
            "image": "/akadem2_photo/27.jpg",
            "category": "duz",
            "price": "79",
            "title": "efsane"
        },
        {
            "image": "/akadem2_photo/60.jpg",
            "category": "damask",
            "price": "50",
            "title": "baya iyi"
        },
        {
            "image": "/akadem2_photo/103.jpg",
            "category": "cizgili",
            "price": "80",
            "title": "çok güzel"
        }
    ]
}

data3 = {
    "akadem3": [
        {
            "image": "/akadem3_photo/27.jpg",
            "category": "duz",
            "price": "79",
            "title": "efsane"
        },
        {
            "image": "/akadem3_photo/60.jpg",
            "category": "damask",
            "price": "50",
            "title": "baya iyi"
        },
        {
            "image": "/akadem3_photo/103.jpg",
            "category": "cizgili",
            "price": "80",
            "title": "çok güzel"
        }
    ]
}

data4 = {
    "akadem4": [
        {
            "image": "/akadem4_photo/27.jpg",
            "category": "duz",
            "price": "79",
            "title": "efsane"
        },
        {
            "image": "/akadem4_photo/60.jpg",
            "category": "damask",
            "price": "50",
            "title": "baya iyi"
        },
        {
            "image": "/akadem4_photo/103.jpg",
            "category": "cizgili",
            "price": "80",
            "title": "çok güzel"
        }
    ]
}

data5 = {
    "serisonu": [
        {
            "image": "/serisonu_photo/27.jpg",
            "price": "79",
            "title": "efsane"
        },
        {
            "image": "/serisonu_photo/60.jpg",
            "price": "50",
            "title": "baya iyi"
        }
    ]
}

data6 = {
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

data7 = {
    "blog": [
        {
            "image": "/blog_photo/blog1.jpg",
            "title": "duvar kağıdı",
            "description": "description yazısı"
        },
        {
            "image": "/blog_photo/blog.jpg",
            "title": "duvar çıtası",
            "description": "description yazısı"
        }
    ]
}

data8 = {
    "poster": [
        {
            "image": "/poster_photo/poster.jpg",
            "title": "Poster",
            "description": "description yazısı"
        },
        {
            "image": "/poster_photo/poster1.jpg",
            "title": "Poster1",
            "description": "description yazısı"
        }
    ]
}

data9 = {
    "stropiyer": [
        {
            "image": "/stropiyer_photo/stropiyer.jpg",
            "title": "Stropiyer",
            "description": "description yazısı"
        },
        {
            "image": "/stropiyer_photo/stropiyer1.jpg",
            "title": "Stropiyer1",
            "description": "description yazısı"
        }
    ]
}

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

def tavan_kaplama(request):
    return render(request, "tavan_kaplama.html")

def citalama_dekor(request):
    return render(request, "citalama_dekor.html")

def iletisim(request):
    return render(request, "iletisim.html")