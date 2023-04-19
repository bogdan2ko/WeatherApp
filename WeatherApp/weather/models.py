from django.db import models
from django.core.exceptions import ValidationError


class City(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if City.objects.count() < 10:
    #         super().save(*args, **kwargs)
    #     else:
    #         pass
