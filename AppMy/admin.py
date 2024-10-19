from django.contrib import admin
from AppMy.models import *



from .models import Card, Category, SponsorCard, MediaCard

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_live')
    fields = ('title', 'description', 'category', 'image', 'is_live')

    def get_fields(self, request, obj=None):
        fields = list(super(ProjectAdmin, self).get_fields(request, obj))  # tuple'ı listeye dönüştürüyoruz
        allowed_groups = ['is_live_yetki']  # Sadece bu grupların is_live'ı görmesini istiyoruz
        
        if request.user.is_superuser:
            return fields

        # Kullanıcı bu gruplardan birinde değilse is_live alanını kaldır
        if not any(group.name in allowed_groups for group in request.user.groups.all()):
            fields.remove('is_live')
        
        return fields



# SponsorCard için özel Admin sınıfı
class SponsorCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_live')  # SponsorCard listesinde gösterilecek alanlar
    fields = ('title', 'image', 'is_live')  # SponsorCard formundaki alanlar

    def get_fields(self, request, obj=None):
        fields = list(super(SponsorCardAdmin, self).get_fields(request, obj))  # Tuple'ı listeye dönüştürüyoruz
        allowed_groups = ['SponsorAdminGroup', 'SponsorManagerGroup','is_live_yetki']  # SponsorCard için özel gruplar

        # Superuser her zaman is_live alanını görür
        if request.user.is_superuser:
            return fields

        # Eğer kullanıcı bu gruplarda değilse is_live alanını kaldır
        if not any(group.name in allowed_groups for group in request.user.groups.all()):
            if 'is_live' in fields:
                fields.remove('is_live')

        return fields


# MediaCard için özel Admin sınıfı
class MediaCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_live')  # MediaCard listesinde gösterilecek alanlar
    fields = ('image', 'is_live')  # MediaCard formundaki alanlar

    def get_fields(self, request, obj=None):
        fields = list(super(MediaCardAdmin, self).get_fields(request, obj))  # Tuple'ı listeye dönüştürüyoruz
        allowed_groups = ['MediaAdminGroup', 'MediaManagerGroup',"is_live_yetki"]  # MediaCard için özel gruplar

        # Superuser her zaman is_live alanını görür
        if request.user.is_superuser:
            return fields

        # Eğer kullanıcı bu gruplarda değilse is_live alanını kaldır
        if not any(group.name in allowed_groups for group in request.user.groups.all()):
            if 'is_live' in fields:
                fields.remove('is_live')

        return fields





admin.site.register(Card ,ProjectAdmin)
admin.site.register(Category)
admin.site.register(SponsorCard, SponsorCardAdmin)
admin.site.register(MediaCard, MediaCardAdmin)
admin.site.register(ContactMessages)