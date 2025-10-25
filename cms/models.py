from django.db import models

class HeroSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='hero_slides/')
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Slide order")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
