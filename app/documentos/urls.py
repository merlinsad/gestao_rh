from django.urls import path, include
from .views import DocumentoCreate, DocumentoEdit, DocumentoDelete

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name="create_documento"),
    #path('deletar/<int:pk>/',
    #    DocumentoEdit.as_view(), name="edit_documento"),
]