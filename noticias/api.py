from noticias.models import Noticia
from rest_framework import viewsets, permissions
from .serializers import NoticiaSerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()   #getAll
    permission_classes = [permissions.AllowAny] 
    serializer_class = NoticiaSerializer