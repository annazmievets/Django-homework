from django.shortcuts import render
from datetime import datetime
import random
from .models import Expression, StrAnalysis
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index_page(request):
    context = {
        'name': 'Курс "Промышленное программирование"',
        'author': 'Аня Змиевец',
        'page_count': 11,
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

def analyze_string(input_string):
    words = re.findall(r'[a-zA-Zа-яА-ЯёЁ0-9]+', input_string)
    numbers = [word for word in words if word.isdigit()]
    return words, numbers
@login_required
def str2words_page(request):

    if request.method == 'POST':
        input_string = request.POST.get('input_string', '')
        words, numbers = analyze_string(input_string)

        StrAnalysis.objects.create(
            user=request.user,
            input_string=input_string,
            word_count=len(words),
            number_count=len(numbers),
        )

        context = {
            'input_string': input_string,
            'words': words,
            'numbers': numbers,
            'word_count': len(words),
            'number_count': len(numbers),
        }
        return render(request, 'str2words.html', context)

    return render(request, 'str2words.html')

def str_history_page(request):
    history = StrAnalysis.objects.filter(user=request.user)
    context = {
        'history': history
    }
    return render(request, 'strhistory.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

if not User.objects.filter(username='vasya').exists():
    User.objects.create_user(username='vasya', password='promprog')
    print("Пользователь vasya создан.")