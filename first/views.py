from django.shortcuts import render
from datetime import datetime
import random

def index_page(request):
    context = {
        'name': 'Курс "Промышленное программирование"',
        'author': 'Аня Змиевец',
        'page_count': 5,
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

history = []

def generate_expression():
    a1 = random.randint(10, 99)
    a2 = random.randint(10, 99)
    a3 = random.randint(10, 99)
    a4 = random.randint(10, 99)
    op1 = random.choice(['+', '-'])
    op2 = random.choice(['+', '-'])

    expression = f'{a1} {op1} {a2} {op2} {a3} {op2} {a4}'
    result = eval(expression)
    return expression, result

def expression_page(request):
    expression, result = generate_expression()

    history.append({'expression': expression, 'result': result})
    context = {
        'name': 'Курс "Промышленное программирование"',
        'expression': expression,
        'result': result
    }

    return render(request, 'expression.html', context)

def history_page(request):

    context = {
        'name': 'Курс "Промышленное программирование"',
        'history': history
    }

    return render(request, 'history.html', context)
