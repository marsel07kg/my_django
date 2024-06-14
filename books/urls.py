from books import views
from django.urls import path
from . import views


urlpatterns = [
    path('all_products/' ,views.all_products),
    path('manga/', views.manga_view),
    path('comics/', views.comics_view),
    path('another thing/', views.another_things_view),



    path('employees/',views.book_list_views),
    path('employees/<int:id>/', views.book_detail_views),
    path('employees/<int:id>/delete/', views.drop_book_view),
    path('employees/<int:id>/update/', views.edit_book_view),
    path('create_book/', views.create_book_view),


    path('hello/',views.name_age),
    path('bio/', views.bio),
    path('number/', views.random_number),
    path('time/', views.current_time)
]