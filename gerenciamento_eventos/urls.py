from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from eventos.views import LocalViewSet, EventoViewSet, CustoViewSet

router = DefaultRouter()
router.register(r'locais', LocalViewSet, basename='locais')
router.register(r'eventos', EventoViewSet, basename='eventos')
router.register(r'custos', CustoViewSet, basename='custos')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls))
]
    