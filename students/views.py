from datetime import datetime, timedelta
from collections import OrderedDict

from django.views.generic import View
from django.utils.timezone import localtime
from django.template.response import TemplateResponse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.contrib import messages
from django.views.decorators.cache import patch_cache_control

from accounts.models import User
from common.classviews import (ModelView, TemplateView, FormView,
    CreateView, UpdateView, DetailView, DeleteView, ListView)
from common.classviews import mapping2query, query2mapping
from . import forms, models
from . import appname


class ConfigMixin(object):

    model=models.Student
    appname=appname

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        sidebar=OrderedDict()
        sidebar['首页']=self.rvs('home')
        sidebar['列表']=self.rvs('index')   
        sidebar['创建']=self.rvs('create')  
        if 'pk' in self.kwargs:
            pk=self.kwargs['pk']
            sidebar['查看']=self.rvs('detail',pk=pk)
            sidebar['更新']=self.rvs('update',pk=pk)    
            sidebar['删除']=self.rvs('delete',pk=pk)                    
        context['sidebar']=sidebar
        return context

    def get_template_names(self):
        if self.template_name is not None:
            return [self.template_name]
        if self.model is not None:
            return ["%s/%s.html" % (self.model._meta.app_label, 
                type(self).__name__,
            )]
        raise ImproperlyConfigured('找不到模板路径')

class detail(ConfigMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

class create(ConfigMixin, FormView):

    form_class=forms.Student
    template_name='students/form.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

class update(ConfigMixin, FormView):

    form_class=forms.Student
    template_name='students/form.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial.update(model_to_dict(self.object))
        return initial

class index(ConfigMixin, ListView):

    ""
    # def get_queryset(self):
    #     if self.queryset is not None:
    #         return self.queryset._clone()
    #     if self.model is not None:
    #         return self.model._default_manager.all()
    #     msg = "'%s' 要么定义'queryset'或'model',要么重新get_queryset方法"
    #     raise ImproperlyConfigured(msg % self.__class__.__name__)


class delete(ConfigMixin, DeleteView):

    pass