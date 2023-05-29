from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField()
    amount =  models.FloatField(blank=False, null=False)

    def __str__(self):
        return str(self.name)