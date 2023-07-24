from django.contrib import admin
from.models import duvar_Kagidi, duvar_Paneli, stropiyer, tavan_Kaplama, citalama_Dekor

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'image')
    # search_fields = ['title', 'content']

admin.site.register(duvar_Kagidi, ArticleAdmin)
admin.site.register(duvar_Paneli)
admin.site.register(stropiyer, ArticleAdmin)
admin.site.register(tavan_Kaplama, ArticleAdmin)
admin.site.register(citalama_Dekor, ArticleAdmin)
       
    
