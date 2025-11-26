from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('catalog/', views.catalog, name='catalog'),
    path('catalog/phones/', views.phones, name='phones'),
    path('catalog/phones/apple/', views.apple, name='apple'),
    path('catalog/phones/samsung/', views.samsung, name='samsung'),
    path('catalog/laptops/', views.laptops, name='laptops'),

    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),

    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('offer/', views.offer, name='offer'),
]
