from django.urls import path
from . import views

urlpatterns = [
    path('' , views.lista_f1, name='lista_f1')
]