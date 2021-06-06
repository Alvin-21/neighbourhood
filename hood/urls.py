from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='homepage'),
    re_path(r'^hood/(\d+)', views.hood, name='hood'),
    re_path(r'^profile/(\d+)', views.profile, name='profile'),
    re_path(r'^new/neighbourhood$', views.create_hood, name='new_neighbourhood'),
    re_path(r'^new/business/hood-id/(\d+)$', views.create_business, name='new_business'),
    re_path(r'^new/post/hood-id/(\d+)$', views.create_post, name='new_post'),
    re_path(r'^edit/profile/(\d+)$', views.edit_profile, name='edit_profile'),
]