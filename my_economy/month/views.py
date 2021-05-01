from django.shortcuts import render, redirect
from django.http import Http404

from .models import Month
from .forms import MonthModelForm, CSVForm

def month_list(request):
    months = Month.objects.all()
    return render(request, 'month/month_list.html', {'months': months})

def month_detail(request, month, year):
    try:
        month = Month.objects.get(name=month, year=year)
        return render(request, 'month/month_detail.html', {'month': month})
    except Month.DoesNotExist:
        raise Http404(f'Month {month} of {year} not exist')

def create(request):
    if request.method == 'GET':
        initial_data = {
            'year': 2021,
            'name': 'Enero',
            'expenses': 100,
        }
        if 'create' in request.path:
            form = MonthModelForm(initial=initial_data)
        else:
            form = CSVForm()
        return render(request, "month/form.html", {'form':form})
    else:
        file = request.FILES.get('file', None)
        if not file:
            form = MonthModelForm(request.POST, request.FILES)
        else:
            form = CSVForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                month = form.save()
            except Exception as e:
                return render(request, "month/form.html", {'form': form, 'error': e.message})
            if not file:
                return redirect('month', month=month.name, year=month.year)
            else:
                return redirect('months')
        return render(request, "month/form.html", {'form':form})


