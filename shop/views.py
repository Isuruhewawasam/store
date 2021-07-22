from django.shortcuts import render
from django.views.generic import TemplateView
from.models import *

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        contex= super().get_context_data(**kwargs)
        contex['my_name']='isuru'
        contex['catergory']=catergory.objects.all()
        return contex


class productView(TemplateView):
    template_name='product.html'

    def get_context_data(self, **kwargs):
        contex= super().get_context_data(**kwargs)
        contex['product']=product.objects.all()
        return contex
    

