from django.shortcuts import render, redirect
from .models import Table
from .forms import TableForm


def index(request):
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту'})


def table(request):
    tables = Table.objects.all()
    return render(request, 'main/table.html', {'title': 'Таблиці', 'tables': tables})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table-1')
        else:
            error = 'Форма введена невірно'
    form = TableForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

