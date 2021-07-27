

from django.urls import path
from .views import catView,product, productView

urlpatterns = [
    path('',productView.as_view(),name='home'),
    path('catergory/',catView.as_view(),name='catergory'),
    
]
