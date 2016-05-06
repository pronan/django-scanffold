import os

from django.conf.urls import patterns, url  
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import user_passes_test, login_required as lr
from django.forms.models import model_to_dict
from django.views.decorators.cache import cache_control

from . import views

sur = user_passes_test(lambda u:u.is_staff) 

index = views.index.as_view(menu="列表")
home = index
create = views.create.as_view(menu="创建")
update = views.update.as_view(menu="更新")
delete = views.delete.as_view(menu="删除")
detail = views.detail.as_view(menu="查看")


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^index/$',  index, name='index'), 
    url(r'^create/$',  create, name='create'), 
    url(r'^(?P<pk>\d+)/update/$', update, name='update'), 
    url(r'^(?P<pk>\d+)/detail/$', detail, name='detail'), 
    url(r'^(?P<pk>\d+)/delete/$', delete, name='delete'), 
]