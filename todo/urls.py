from django.urls import path
from .views import (
    home_page,
    todo_list,
    todo_detail,
    todo_create,
    todo_update,
    todo_delete,
) 

app_name = 'todos'

urlpatterns = [
    path('', home_page, name='home'),
    path('create/', todo_create, name='create'),
    path('list/', todo_list, name='list'),
    path('update/<id>/', todo_update, name='update'),
    path('delete/<id>/', todo_delete, name='delete'),
    path('<id>/', todo_detail, name='details'),

]
