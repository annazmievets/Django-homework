from django.shortcuts import render

def index_page(request):
    context = {
        'name': 'Курс "Промышленное программирование"',
        'author': 'Аня Змиевец',
        'page_count': 3,
    }
    return render(request, 'index.html', context)