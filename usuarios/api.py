from usuarios.models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()   #getAll
    permission_classes = [permissions.AllowAny] 
    serializer_class = UsuarioSerializer