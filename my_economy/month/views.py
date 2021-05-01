from django.shortcuts import render
from django.http import Http404

from .models import Month

def month_list(request):
    months = Month.objects.all()
    return render(request, 'month/month_list.html', {'months': months})

def month_detail(request, month, year):
    try:
        month = Month.objects.get(name=month, year=year)
        return render(request, 'month/month_detail.html', {'month': month})
    except Month.DoesNotExist:
        raise Http404(f'Month {month} of {year} not exist')
