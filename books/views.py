from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime

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
