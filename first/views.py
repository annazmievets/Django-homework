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