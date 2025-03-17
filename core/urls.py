from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import AmazoneViewSet
router = DefaultRouter()
router.register(r'resultsdata', AmazoneViewSet)

urlpatterns = [
    path('',views.amazonscrapedata,name="amazonscrapedata"),
    path('api/',include(router.urls)),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)