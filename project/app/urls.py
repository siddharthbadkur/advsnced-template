
from django.urls import path
from .views import *

urlpatterns= [
    path('home/',home,name='home'),
    path('contact/',contact,name='contact'),
    path('about/',home,name='about'),
    path('survey/',survey,name='survey')
]