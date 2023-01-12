
from django.urls import path
from . import views

''' Crear las rutas en una lista de nombre urlpatterns '''
urlpatterns = [
    path('', views.compras, name='compras'),
                                #tiene que coincidir con el action
    path('nuevo',views.nuevo,name='nuevo'),
    
    path('comprado/<int:identificador>',views.comprado,name="comprado"),
    
    path('anadir/<int:identificador>',views.anadir,name="anadir"),
]