from django.urls import path

from . import views     # it means - 'from all import views'

urlpatterns = [
    path('',views.index, name='index'),
    path('mail',views.send,name='mail')
]