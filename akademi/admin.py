from django.contrib import admin
from .models import duvar_Paneli, stropiyer_Model, tavan_Kaplama, citalama_Dekor, akadem1_Model, akadem2_Model, akadem3_Model, serisonu_Model, akadem4_Model, blog_Model, poster_Model, aka_Kids
from django.conf import settings
import os

class ImageModelAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        # Dosyayı diskten sil
        os.remove(os.path.join(settings.MEDIA_ROOT, str(obj.image)))
        # Veritabanında kaydı sil
        obj.delete()

class akadem1_ModelAdmin(ImageModelAdmin):  
    pass

class akadem2_ModelAdmin(ImageModelAdmin):  
    pass

class akadem3_ModelAdmin(ImageModelAdmin):  
    pass

class akadem4_ModelAdmin(ImageModelAdmin):
    pass

class serisonu_ModelAdmin(ImageModelAdmin):  
    pass

class duvar_PaneliAdmin(ImageModelAdmin):  
    pass

class poster_ModelAdmin(ImageModelAdmin):
    pass

class blog_ModelAdmin(ImageModelAdmin):  
    pass

class stropiyer_ModelAdmin(ImageModelAdmin):
    pass

class aka_KidsAdmin(ImageModelAdmin):
    pass

class tavan_KaplamaAdmin(ImageModelAdmin):
    pass

class citalama_DekorAdmin(ImageModelAdmin):
    pass

admin.site.register(akadem1_Model, akadem1_ModelAdmin)
admin.site.register(akadem2_Model, akadem2_ModelAdmin)
admin.site.register(akadem3_Model, akadem3_ModelAdmin)
admin.site.register(akadem4_Model, akadem4_ModelAdmin)
admin.site.register(serisonu_Model, serisonu_ModelAdmin)
admin.site.register(duvar_Paneli, duvar_PaneliAdmin)
admin.site.register(poster_Model, poster_ModelAdmin)
admin.site.register(blog_Model, blog_ModelAdmin)
admin.site.register(stropiyer_Model, stropiyer_ModelAdmin)
admin.site.register(tavan_Kaplama, tavan_KaplamaAdmin)
admin.site.register(citalama_Dekor, citalama_DekorAdmin)
admin.site.register(aka_Kids, aka_KidsAdmin)
