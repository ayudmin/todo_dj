from django.urls import path
from .views import (

    todo_list, 
    todo_detail, 
    todo_create, 
    todo_update,
    todo_delete,
)

app_name = 'todos'

urlpatterns = [
    path('', todo_list, name='home'),
    path('create/', todo_create, name='create'),
    path('<int:id>/', todo_detail, name='detail'),
    path('<int:id>/update/', todo_update, name='update'),
    path('<int:id>/delete/', todo_delete, name='delete')
]