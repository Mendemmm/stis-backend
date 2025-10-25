from django.contrib import admin
from .models import HeroSlide

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image', 'link')
