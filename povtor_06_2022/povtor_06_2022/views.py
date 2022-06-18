# в этом файле хранятся функции представления, что должно произойти по кокому-то конкретному пути

from django.http import HttpResponse
from django.shortcuts import render #импорт рендер из ярлыков

def about(request):
    return render(request, 'about.html', {'key1': 'Значение переменной - key1'})

def home(request):
    return HttpResponse('This is my HOME')
