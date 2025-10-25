from rest_framework import serializers
from .models import HeroSlide

class HeroSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlide
        fields = ['id', 'title', 'subtitle', 'image', 'link', 'order']
