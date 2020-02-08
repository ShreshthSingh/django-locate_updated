from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.hostel,name = 'hostel'),
    path('find',views.find,name = 'find')
     
    
]
