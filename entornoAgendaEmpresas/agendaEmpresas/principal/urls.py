from django.urls import path
from .views import EmpresaListView,EmpresaDetailView,EmpresaCreateView

urlpatterns=[
    path('',EmpresaListView.as_view(),name='listado'),
    path('crearEmpresa',EmpresaCreateView.as_view(),name='crear'),
    path('empresa/<int:pk>',EmpresaDetailView.as_view(),name='detalle'),
    
]