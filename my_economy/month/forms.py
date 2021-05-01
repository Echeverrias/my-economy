from django import forms
from django.utils.translation import ugettext_lazy as _
import re
from .models import Month
import pandas as pd
import csv
import io
from datetime import datetime

class MonthModelForm(forms.ModelForm):

    tag = forms.CharField(max_length=20, required=False, widget=forms.TextInput())

    class Meta:
        model = Month
        fields = '__all__'
        help_texts = None
        labels = {'name': _('Mes'), 'year': _('Año'), 'expenses': _('Gastos'), 'income': _('Ingresos')}

    def normalize_month_name(self):
        pass

    def process_file(self):
        file_obj = self.cleaned_data.get('file', None)
        if file_obj:
            file_bytes = file_obj.file
            file_text = io.TextIOWrapper(file_bytes)
            reader = csv.DictReader(file_text)
            columns = reader.fieldnames
            year = datetime.now().year
            for row in reader:
                for col in columns:
                    print(row[col])
                    print(type(row[col]))
                    month, created = Month.objects.get_or_create(name=col, year=year, defaults={'expenses':float(row[col])})
                    if not created:
                        print(month)
                        month.expenses = float(row[col])
                        month.save()


    def clean_file(self):
        print('clean_file')
        file = self.cleaned_data.get('file', None)
        print(file)
        if file:
            try:
                extension_regex = re.compile('.(\w{2,7})$')
                extension = extension_regex.search(file.name).group(1)
                if extension != 'csv':
                    raise forms.ValidationError('Archivo no válido')
            except Exception as e:
                print(e)
                raise forms.ValidationError('Error al procesar el archivo')
        return file

    def save(self, *args, **kwargs):
        self.process_file()
        name = self.cleaned_data.get('name')
        year = self.cleaned_data.get('year')
        expenses = self.cleaned_data.get('expenses')
        month, created = Month.objects.get_or_create(name=name, year=year, defaults={'expenses': expenses})
        if not created:
            month.expenses = expenses
            month.save()
        return month

class CSVForm(forms.Form):

    file = forms.FileField(label='Archivo', required=False)

    class Meta:
        help_texts = {'file': 'Selecciona un fichero csv'}
        labels = {'name': _('Mes'), 'year': _('Año'), 'expenses': _('Gastos'), 'income': _('Ingresos')}

    def normalize_month_name(self):
        pass

    def process_file(self):
        try:
            file_obj = self.cleaned_data.get('file', None)
            if file_obj:
                file_bytes = file_obj.file
                file_text = io.TextIOWrapper(file_bytes)
                reader = csv.DictReader(file_text)
                columns = reader.fieldnames
                year = datetime.now().year
                for row in reader:
                    for col in columns:
                        print(row[col])
                        print(type(row[col]))
                        month, created = Month.objects.get_or_create(name=col, year=year, defaults={'expenses':float(row[col])})
                        if not created:
                            print(month)
                            month.expenses = float(row[col])
                            month.save()
        except Exception as e:
            print(e)
            raise forms.ValidationError('Error al procesar el archivo')

    def clean_file(self):
        print('clean_file')
        file = self.cleaned_data.get('file', None)
        print(file)
        if file:
            try:
                extension_regex = re.compile('.(\w{2,7})$')
                extension = extension_regex.search(file.name).group(1)
                if extension != 'csv':
                    raise forms.ValidationError('Tipo de archivo no válido')
            except Exception as e:
                if e.__class__.__name__ != 'ValidationError':
                    raise forms.ValidationError('Error al procesar el archivo')
                raise e
        return file

    def save(self, *args, **kwargs):
        self.process_file()


