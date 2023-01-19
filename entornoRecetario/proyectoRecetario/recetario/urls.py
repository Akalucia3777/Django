from django.urls import path
from . import views

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('receta',views.receta,name='receta'),
]