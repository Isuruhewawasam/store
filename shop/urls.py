

from django.urls import path
from .views import HomeView,product, productView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('product/',productView.as_view(),name='home'),
]
