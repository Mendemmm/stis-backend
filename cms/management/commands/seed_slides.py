from django.core.management.base import BaseCommand
from cms.models import HeroSlide

class Command(BaseCommand):
    help = "Seed initial hero slides into the database"

    def handle(self, *args, **options):
        slides = [
            {
                "title": "The Roads to Energy Excellence",
                "subtitle": "Delivering reliable inspection, NDT, and engineering solutions that power the oil and gas industry.",
                "image": "slides/slide1.jpg",  # make sure this path matches your MEDIA folder
                "link": "/news/the-roads-to-energy-excellence",
                "order": 1,
            },
            {
                "title": "Safety. Integrity. Innovation.",
                "subtitle": "We uphold the highest standards in pipeline inspection, well completion, and energy operations.",
                "image": "slides/slide2.jpg",
                "link": "/news/the-roads-to-energy-excellence",
                "order": 2,
            },
            {
                "title": "Sustainability Meets Precision",
                "subtitle": "Driving efficient, safe, and environmentally responsible energy practices across upstream and downstream operations.",
                "image": "slides/slide3.jpg",
                "link": "/news/the-roads-to-energy-excellence",
                "order": 3,
            },
        ]

        for slide in slides:
            obj, created = HeroSlide.objects.get_or_create(
                title=slide["title"],
                defaults={
                    "subtitle": slide["subtitle"],
                    "image": slide["image"],
                    "link": slide["link"],
                    "order": slide["order"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added: {obj.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped (already exists): {obj.title}"))
