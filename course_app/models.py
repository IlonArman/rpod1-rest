from django.db import models
from pytils.translit import slugify

class Menu(models.Model):
    name = models.CharField("Menu name", max_length=255)
    description = models.TextField("Menu description")
    slug = models.SlugField(unique=True, blank=True, editable=False)
    
    class Meta:
        verbose_name="Menu"
        verbose_name_plural='Menues'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Dishes(models.Model):
    dishes = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name="Choose menu")
    dish = models.CharField("Menu dish", max_length=255)
    content= models.TextField("Description", blank=True)

    class Meta:
        verbose_name="Dishes"
        verbose_name_plural='Dish'

    def __str__(self):
        return f"{self.menu.name} - {self.dish}"
# Create your models here.
