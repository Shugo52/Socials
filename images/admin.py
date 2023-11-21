from django.contrib import admin
from .models import Image


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'image', 'created_at']
    list_filter = ['created_at']
