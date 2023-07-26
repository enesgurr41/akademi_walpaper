from django.contrib import admin
from .models import duvar_Kagidi, duvar_Paneli, stropiyer, tavan_Kaplama, citalama_Dekor, akadem1_Model, akadem2_Model, akadem3_Model, serisonu_Model
from django.conf import settings
import os

class ImageModelAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        # Dosyayı diskten sil
        os.remove(os.path.join(settings.MEDIA_ROOT, str(obj.image)))
        # Veritabanında kaydı sil
        obj.delete()

class duvar_KagidiAdmin(ImageModelAdmin): 
    pass

class akadem1_ModelAdmin(ImageModelAdmin):  
    pass

class akadem2_ModelAdmin(ImageModelAdmin):  
    pass

class akadem3_ModelAdmin(ImageModelAdmin):  
    pass

class serisonu_ModelAdmin(ImageModelAdmin):  
    pass

admin.site.register(duvar_Kagidi, duvar_KagidiAdmin)
admin.site.register(akadem1_Model, akadem1_ModelAdmin)
admin.site.register(akadem2_Model, akadem2_ModelAdmin)
admin.site.register(akadem3_Model, akadem3_ModelAdmin)
admin.site.register(serisonu_Model, serisonu_ModelAdmin)
admin.site.register(duvar_Paneli)
admin.site.register(stropiyer, ImageModelAdmin)
admin.site.register(tavan_Kaplama, ImageModelAdmin)
admin.site.register(citalama_Dekor, ImageModelAdmin)
