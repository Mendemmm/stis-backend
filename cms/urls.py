from django.urls import path
from .views import HeroSlideListView

urlpatterns = [
    path('hero-slides/', HeroSlideListView.as_view(), name='hero-slides'),
]
