from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("ana-sayfa", views.index, name="ana_sayfa"),
    path("avcilar-duvar-kagidi-deposu-akadem1", views.akadem1, name="avcilar_duvar_kagidi-deposu-akadem1"),
    path("avcilar-duvar-kagidi-deposu-akadem2", views.akadem2, name="avcilar_duvar_kagidi-deposu-akadem2"),
    path("avcilar-duvar-kagidi-deposu-akadem3", views.akadem3, name="avcilar_duvar_kagidi-deposu-akadem3"),
    path("avcilar-duvar-kagidi-deposu-akadem4", views.akadem4, name="avcilar_duvar_kagidi-deposu-akadem4"),
    path("avcilar-duvar-kagidi-deposu-serisonu", views.serisonu, name="avcilar_duvar_kagidi-deposu-serisonu"),
    path("stropiyer-duvar-kaplama-fjg3x", views.duvar_paneli, name="stropiyer-duvar-kaplama-fjg3x"),
    path("stropiyer-kartonpiyer-avcilar", views.stropiyer, name="stropiyer-kartonpiyer-avcilar"),
    path("stropiyer-avcilar-tavan-kaplama", views.tavan_kaplama, name="stropiyer-avcilar-tavan-kaplama"),
    path("salon-çıta-koridor", views.citalama_dekor, name="salon-cita-koridor"),
    path("iletisim", views.iletisim, name="iletisim"),
    path("blog", views.blog, name="blog"),
    path("avcilar-duvar-kagidi-deposu-poster", views.poster, name="avcilar_duvar_kagidi-deposu-poster"),
    path("avcilar-duvar-kagidi-deposu-akakids", views.akakids, name="avcilar_duvar_kagidi-deposu-akakids"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)