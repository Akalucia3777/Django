from django.urls import path
from . import views
from .views import CamionListView,CamionDetailView,CamionCreateView,CamionUpdateView,CamionDeleteView

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('todas',CamionListView.as_view(),name='listado'),
    path('camion/<int:pk>',CamionDetailView.as_view(),name='detalle'),
    path('categoria/<int:idCategoria>',views.categoria,name='categoria'),
    path('crearCamion',CamionCreateView.as_view(),name='crear'),
    path('modificarCamion/<int:pk>',CamionUpdateView.as_view(),name='modificar'),
    path('borrarCamion/<int:pk>',CamionDeleteView.as_view(),name='borrar'),
]