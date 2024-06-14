from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
import random
import datetime


def manga_view(request):
    if request.method == 'GET':
        manga_tags = models.library.objects.filter(tags__name='manga').order_by('-id')
        return render(
            request,
            template_name='products/manga_tag.html',
            context={'manga_tags': manga_tags},
        )

def comics_view(request):
    if request.method == 'GET':
        comics_tags = models.library.objects.filter(tags__name='comic').order_by('-id')
        return render(
            request,
            template_name='products/comics_tags.html',
            context={'comics_tags': comics_tags},
        )

def another_things_view(request):
    if request.method == 'GET':
        another_things_tags = models.library.objects.filter(tags__name='another thing').order_by('-id')
        return render(
            request,
            template_name='products/another_things_tag.html',
            context={'another_things_tags': another_things_tags},
        )
def all_products(request):
    if request.method == 'GET':
        products = models.library.objects.filter().order_by('-id')
        return render(
            request,
            template_name='products/all_products.html',
            context={
                'products': products
            }
        )

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
