from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='homepage'),
    re_path(r'^hood/(\d+)', views.hood, name='hood'),
    re_path(r'^profile/(\d+)', views.profile, name='profile'),
    re_path(r'^new/neighbourhood$', views.create_hood, name='new_neighbourhood'),
]