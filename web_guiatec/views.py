from django.views.generic import TemplateView, View, FormView
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, HttpResponse
from django.conf import settings
from io import BytesIO
import qrcode


class TemplateIndex(TemplateView):
    
    template_name = "index.html"


class TemplateTechnicalSupport(TemplateView):

    template_name = "technical_support.html"


class TemplateSoftware(TemplateView):

    template_name = "software.html"


class TemplateContactView(View):
    """view to send form mail"""
           
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
            html_content = "<p>Nombre: {} <br> Asunto: {} <br> Telefono: {} <br>Email:<strong> {} </strong><br> Mensaje:<br> {}.</p>".format(full_name, subject, number, email, content)
            msg = EmailMultiAlternatives('Contac WEb Guiatec {}'.format(full_name), text_content, from_email, [from_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return render (request, 'contact.html', context={'form_valid':True})
        
        return render (request, 'contact.html', context={})


class TemplateQRView(FormView):
    """view to generate QR"""
           
    def get(self, request, *args, **kwargs):
        
        return render (request, 'generateqr.html', context={})

    def post(self, request, *args, **kwargs):

        name_qr = self.request.POST['name_qr']
        text_qr = self.request.POST['text_qr']        

        if name_qr and text_qr :
            
            img = qrcode.make(text_qr)   
            buf = BytesIO()	
            img.save(buf)
            image_stream = buf.getvalue()
            response = HttpResponse (image_stream, 'generateqr.html', headers={
                'content_type':"image/png",
                'Content-Disposition':'attachment; filename="{}.jpeg"'.format(name_qr),'valid':'afjhskasbf'}
                )                            
            return response
        
        return render (request, 'generateqr.html', context={})
