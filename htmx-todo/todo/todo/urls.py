from django.contrib import admin
from django.urls import path

from htmx.views import todos

urlpatterns = [
    path('', todos, name='todos'),
    path('admin/', admin.site.urls),
]
