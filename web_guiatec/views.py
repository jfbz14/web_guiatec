from django.views.generic import TemplateView, View, FormView
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.conf import settings





class TemplateIndex(TemplateView):
    
    template_name = "index.html"


class TemplateTechnicalSupport(TemplateView):

    template_name = "technical_support.html"


class TemplateSoftware(TemplateView):

    template_name = "software.html"


class TemplateContactView(FormView):

           
    def get(self, request, *args, **kwargs):
        
        return render (request, 'contact.html', context={})

    def post(self, request, *args, **kwargs):

        full_name = self.request.POST['full_name']
        email = self.request.POST['email']
        number = self.request.POST['number']
        subject = self.request.POST['subject']
        content = self.request.POST['content']

        if full_name and email and number and object and content :

            from_email = settings.EMAIL_HOST_USER
            text_content = "This is an important message."
            html_content = "<p>{} <br> Asunto:{} <br> <strong>email {} </strong><br> Mensaje:<br> {}.</p>".format(full_name, subject, email, content)
            msg = EmailMultiAlternatives('Contac WEb Guiatec {}'.format(full_name), text_content, from_email, [from_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return render (request, 'contact.html', context={'form_valid':True})
        
        return render (request, 'contact.html', context={})
