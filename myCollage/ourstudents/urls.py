

from django.urls import path
from . import views


urlpatterns = [
    path('aiml/', views.aiml_student, name='aiml_student'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

]