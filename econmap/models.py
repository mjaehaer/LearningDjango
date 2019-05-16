from django.db import models


# Create your models here.
class Category:
    name = models.CharField()
    slug = models.SlugField()