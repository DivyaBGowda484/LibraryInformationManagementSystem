from django.urls import path
from .views import *

urlpatterns = [
    path('', home), 
    path('home', home),
    path('readers', readers),
    path('save', save_student),
    path('readers/add', save_reader),
]
