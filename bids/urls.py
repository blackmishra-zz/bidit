from django.urls import path, include
from . import views

urlpatterns = [
    path('about', views.about, name= 'about'),
    path('create', views.create, name= 'create'),
    path('category', views.category, name= 'category'),
    path('contact', views.contact, name= 'contact'),
    path('cart', views.cart, name= 'cart'),
    path('<int:product_id>', views.details, name= 'details'),  
    path('send_mess', views.send_mess, name= 'send_mess'),  
]
