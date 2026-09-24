from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('courselist/', views.course_list, name='course_list'),
    path('course_detail/', views.course_detail, name='course_detail'),


    # path('blog/<int:blog_year>/<str:blog_month>/', views.blog_detail, name='blog_detail'),

    # re_path(r'^blog/(?P<blog_year>[0-9]{4})/(?P<blog_month>[\w-]+)/$', views.blog_detail, name='blog_detail_regex'),


]