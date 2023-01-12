from django.urls import path
from . import views

urlpatterns = [
    path('',views.propositos,name='propositos'),
    path('nuevProp',views.nuevProp,name='nuevProp'),
    path('conseguido/<int:identificador>',views.conseguido,name='conseguido'),
    path('resetear/<int:identificador>',views.anadir,name='anadir'),
    path('borrar/<int:identificador>',views.borrar,name="borrar"),
    path('modificarNombre/<int:identificador>',views.modificarNombre,name="modificarNombre"),
    path('modificarNombre/actualizar/<int:identificador>',views.actualizar,name="actualizar"),
    path('modificarFech/<int:identificador>',views.modificarFech,name="modificarFech"),
    path('modificarFech/retrasarFech/<int:identificador>',views.retrasarFech,name="retrasarFech"),
]
