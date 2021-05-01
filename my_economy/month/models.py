from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Month (models.Model):

    name = models.CharField(max_length=10)
    year = models.IntegerField(null=False, validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    expenses = models.DecimalField(max_digits=6, decimal_places=2)
    income = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.year}'

    def save(self, *args, **kwargs):
        return super(Month, self).save(*args, **kwargs)

