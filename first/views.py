from django.shortcuts import render
from datetime import datetime
import random
from .models import Expression

def index_page(request):
    context = {
        'name': 'Курс "Промышленное программирование"',
        'author': 'Аня Змиевец',
        'page_count': 8,
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
    Expression.objects.create(expression=expression, result=result)

    context = {
        'name': 'Курс "Промышленное программирование"',
        'expression': expression,
        'result': result
    }

    return render(request, 'expression.html', context)

def history_page(request):
    all = Expression.objects.all()
    context = {
        'name': 'Курс "Промышленное программирование"',
        'history': all
    }

    return render(request, 'history.html', context)

def delete_page(request):
    if Expression.objects.exists():
        Expression.objects.last().delete()
        message = "Удалено последнее выражение из истории"
    else:
        message = "В истории выражений нет записаных выражений"
    context = {
        'message': message
    }
    return render(request, 'delete.html', context)

def clear_page(request):
    Expression.objects.all().delete()
    context = {
        'message': "История выражений очищена"
    }
    return render(request, 'clear.html', context)


def new_page(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    d = request.GET.get('d')
    if a and b and c and d:
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
        except ValueError:
            message = "Введите целые числа"
            context = {
                'message': message
            }
            return render(request, 'new.html', context)
        expression = f'{a} + {b} - {c} - {d}'
        result = a + b - c - d
        Expression.objects.create(expression=expression, result=result)

        message = "Ваше выражение добавлено"
        context = {
            'message': message
        }
        return render(request, 'new.html', context)

    else:
        message = "Чтобы добавить выражение, используйте формат: /new/?a=1&b=2&c=3&d=4"
        context = {
            'message': message
        }
        return render(request, 'new.html', context)