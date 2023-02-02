from django.urls import path
from . import views
from .views import RecetaCreateView,RecetaUpdateView,RecetaDeleteView,RecetaDetailView,RecetaListView

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('receta',views.receta,name='receta'),
    path('desayunos',views.desayunos,name='desayunos'),
    path('comidas',views.comidas,name='comidas'),
    path('cenas',views.cenas,name='cenas'),
    path('todas',RecetaListView.as_view(),name='listado'),
    path('empresa/<int:pk>',RecetaDetailView.as_view(),name='detalle'),
    path('categoria/<int:idCategoria>',views.categoria,name='categoria'),
    path('crearReceta',RecetaCreateView.as_view(),name='crear'),
    path('modificarReceta/<int:pk>',RecetaUpdateView.as_view(),name='modificar'),
    path('borrarReceta/<int:pk>',RecetaDeleteView.as_view(),name='borrar'),
]