from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addproperty/', views.add_property, name='add_property'),
]