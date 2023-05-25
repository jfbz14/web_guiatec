from django.contrib import admin
from django.urls import path
from .views import TemplateIndex, TemplateTechnicalSupport, TemplateSoftware, TemplateContactView, TemplateQRView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateIndex.as_view(), name='index'),
    path('soporte-tecnico-de-computadoras/', TemplateTechnicalSupport.as_view(), name='technical_support'),
    path('desarrollo-de-software/', TemplateSoftware.as_view(), name='software'),
    path('aplicaciones-web/', TemplateContactView.as_view(), name='contact'),
    path('generate_QR/', TemplateQRView.as_view(), name='QR'),
]
