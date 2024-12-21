from django.shortcuts import render
from datetime import datetime

def index_page(request):
    context = {
        'name': 'Курс "Промышленное программирование"',
        'author': 'Аня Змиевец',
        'page_count': 3,
    }
    return render(request, 'index.html', context)

def time_page(request):
    now = datetime.now()
    context = {
        'name': 'Курс "Промышленное программирование"',
        'date': now.strftime('%d.%m.%Y'),
        'time': now.strftime('%H:%M:%S'),
    }
    return render(request, 'time.html', context)

def calc_page(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        a = 0
        b = 0

    summ = a + b

    context = {
        'name': 'Курс "Промышленное программирование"',
        'first': a,
        'second': b,
        'sum': summ,
    }
    return render(request, 'calc.html', context)