from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # site_administration
    path('admin/', admin.site.urls),
    # todo_app_urls
    path('', include('todo.urls', namespace='todos')),


]
