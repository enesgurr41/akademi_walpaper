from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("ana-sayfa", views.index, name="ana_sayfa"),
    path("avcilar-duvar-kagidi-deposu-vinil", views.duvar_kagidi, name="avcilar_duvar_kagidi-deposu-vinil"),
    path("avcilar-duvar-kagidi-deposu-akadem1", views.akadem1, name="avcilar_duvar_kagidi-deposu-akadem1"),
    path("stropiyer-duvar-kaplama-fjg3x", views.duvar_paneli, name="strpoyier-duvar-kaplama-fjg3x"),
    path("avcilar-duvar-kagidi-deposu-akadem2", views.akadem2, name="avcilar_duvar_kagidi-deposu-akadem2"),
    path("avcilar-duvar-kagidi-deposu-akadem3", views.akadem3, name="avcilar_duvar_kagidi-deposu-akadem3"),
    path("stropiyer-kartonpiyer-avcilar", views.stropiyer, name="stropiyer-kartonpiyer-avcilar"),
    path("stropiyer-avcilar-tavan-kaplama", views.tavan_kaplama, name="stropiyer-avcilar-tavan-kaplama"),
    path("salon-çıta-koridor", views.citalama_dekor, name="salon-çıta-koridor"),
    path("iletisim", views.iletisim, name="iletisim"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)