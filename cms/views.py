from rest_framework import generics
from .models import HeroSlide
from .serializers import HeroSlideSerializer

class HeroSlideListView(generics.ListAPIView):
    queryset = HeroSlide.objects.all()
    serializer_class = HeroSlideSerializer
