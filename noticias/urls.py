import imp
from rest_framework import routers
from .api import NoticiaViewSet

router = routers.DefaultRouter()

router.register('api/noticias', NoticiaViewSet, 'noticias')

urlpatterns = router.urls