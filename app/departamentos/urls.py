from django.urls import path, include
from .views import DepartamentosList, DepartamentoCreate, DepartamentoDelete, DepartamentoEdit

urlpatterns = [
    path('list', DepartamentosList.as_view(), name="list_departamentos"),
    path('novo', DepartamentoCreate.as_view(), name="create_departamento"),
    path('delete/<int:pk>/', DepartamentoDelete.as_view(), name="delete_departamento"),
    path('editar/<int:pk>/', DepartamentoEdit.as_view(), name="update_departamento")
]