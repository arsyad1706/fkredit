from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='form'),
    path('addform', views.addform, name="addform"),
    path('success', views.modal, name="modal"),
]
