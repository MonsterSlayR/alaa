
from django.db import models
from django.utils.html import format_html

class Service(models.Model):
    SERVICE_ICONS = [
        ('ri-sword-fill', 'Sword (Mythic+)'),
        ('ri-trophy-fill', 'Trophy (Raid)'),
        ('ri-shield-star-fill', 'Shield (PvP)'),
        ('ri-bar-chart-fill', 'Chart (Leveling)'),
        ('ri-treasure-map-fill', 'Treasure (Mounts)'),
        ('ri-coins-fill', 'Coins (Gold)'),
        # Add more icons as needed
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=SERVICE_ICONS)
    modal_id = models.SlugField(max_length=50, unique=True, help_text="Used for the modal ID (e.g., 'mythicModal')")
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which services appear")

    # Modal content fields
    modal_title = models.CharField(max_length=100)
    modal_description = models.TextField()
    title_top = models.CharField(max_length=100 ,default="features :" )
    modal_features = models.TextField(help_text="One feature per line")
    title_left = models.CharField(max_length=100 , default="pricing :")
    modal_pricing_left = models.TextField(help_text="Pricing left column (One item per line)")
    title_right= models.CharField(max_length=100, default="pricing :")
    modal_pricing_right = models.TextField(help_text="Pricing right column (One item per line)")
    url= models.CharField(max_length=600 , default=" ")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def icon_preview(self):
        return format_html(f'<i class="{self.icon} ri-2x"></i>')
    icon_preview.short_description = 'Icon Preview'