from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
