from django.urls import path
from . import views

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('receta',views.receta,name='receta'),
    path('desayuno',views.desayuno,name='desayuno'),
    path('comidas',views.comidas,name='comidas'),
    path('cenas',views.cenas,name='cenas'),
    path('todas',views.todas,name='todas'),
]