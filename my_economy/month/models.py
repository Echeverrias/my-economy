from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Month (models.Model):

    months = [
        ('Enero', 'Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre'),
    ]

    name = models.CharField(max_length=10, choices=months)
    year = models.IntegerField(null=False, validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    expenses = models.DecimalField(max_digits=6, decimal_places=2)
    income = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.year} - expenses: {self.expenses}'

    def save(self, *args, **kwargs):
        return super(Month, self).save(*args, **kwargs)

