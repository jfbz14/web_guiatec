from django.contrib import admin
from django.urls import path
from .views import TemplateIndex, TemplateTechnicalSupport

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateIndex.as_view(), name='index'),
    path('soporte-tecnico-de-computadoras/', TemplateTechnicalSupport.as_view(), name='technical_support'),
]
