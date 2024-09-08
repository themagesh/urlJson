from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.name_url_form, name='name_url_form'),
    path('success/', views.success, name='success'),
]
