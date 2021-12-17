from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gallery import models


# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'id_art','author', 'title', 'year', 'material', 'paints', 'sizeW', 'sizeH', 'location', 'owner', 'comment', 'checked')
    search_fields = ('title', 'id_art', 'year', 'comment')


admin.site.register(models.Author)
admin.site.register(models.Gallery, GalleryAdmin)
admin.site.register(models.Location)
admin.site.register(models.Material)
admin.site.register(models.Paints)
admin.site.register(models.Owner)
admin.site.register(models.Signature)
admin.site.site_header = 'Панель администратора'
admin.site.site_title = 'Панель администратора'
