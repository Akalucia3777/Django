from django.urls import path
from .views import ProfesoresListView,ProfesoresCreateView,ProfesoresUpdateView,ProfesoresDeleteView




urlpatterns=[
    path('',ProfesoresListView.as_view(),name='listado'),
    path('crearProfesor',ProfesoresCreateView.as_view(),name='crear'),
    path('modificarProfesor/<int:pk>',ProfesoresUpdateView.as_view(),name='modificar'),
    path('borrarProfesor/<int:pk>',ProfesoresDeleteView.as_view(),name='borrar'),
]