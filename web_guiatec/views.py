from django.shortcuts import render
from django.views.generic import TemplateView


class TemplateIndex(TemplateView):
    
    template_name = "index.html"


class TemplateTechnicalSupport(TemplateView):

    template_name = "technical_support.html"


