from books import views
from django.urls import path

urlpatterns = [
    path('hello/',views.name_age),
    path('bio/', views.bio),
    path('number/', views.random_number),
    path('time/', views.current_time)
]