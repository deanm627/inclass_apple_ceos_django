from django.db import models

# Create your models here.
class CEO(models.Model):
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=80)
    first_year_active = models.IntegerField()

    def __str__(self):
        return self.name