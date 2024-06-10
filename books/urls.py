from books import views
from django.urls import path
from . import views
import random

urlpatterns = [
    path('employees/',views.book_list_views),
    path('employees/<int:id>/', views.book_detail_views),


    path('hello/',views.name_age),
    path('bio/', views.bio),
    path('number/', views.random_number),
    path('time/', views.current_time)
]