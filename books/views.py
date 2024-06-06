from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
import random
import datetime

def book_detail_views(request, id):
    if request.method == 'GET':
        emp_id = get_object_or_404(models.Employees, id=id)
        return render(
            request,
            template_name='employees/book_detail.html',
            context={
                'emp_id': emp_id,
            }
        )

def book_list_views(request):
    if request.method == 'GET':
        queryset = models.Employees.objects.filter().order_by('-id')
        return render(
            request,
            template_name='employees/book_list.html',
            context={
                'emp': queryset
            }
        )

def name_age(request):
    if request.method == 'GET':
        return HttpResponse("Привет меня зовут Бекболотов Марсель мне 17 лет")

def bio(request):
    if request.method == 'GET':
        return HttpResponse("кубик рубик, шахматы, теннис, программирование")

def random_number(request):
    if request.method == 'GET':
        number = random.randint(0, 100)
        return HttpResponse(number)

def current_time(request):
    if request.method == 'GET':
        time = datetime.datetime.now()
        return HttpResponse(time)
# Create your views here.
