from categorias.models import Categoria
from rest_framework import viewsets, permissions
from .serializers import CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()   #getAll
    permission_classes = [permissions.AllowAny] 
    serializer_class = CategoriaSerializer