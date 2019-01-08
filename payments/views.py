from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class Payment(TemplateView):
    template_name = 'payment.html'