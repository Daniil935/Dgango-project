from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('relevance',views.relevance, name='relevance'),
    path('geography',views.geography, name='geography'),
    path('skills',views.skills, name='skills')
]
