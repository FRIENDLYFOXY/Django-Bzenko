from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'main'),
    path('table', views.table, name = 'table-1'),
    path('create', views.create, name = 'create'),
]