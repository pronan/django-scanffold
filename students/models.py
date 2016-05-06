import re
import os
from itertools import cycle
from datetime import date, datetime
from collections import OrderedDict

from django.utils.safestring import mark_safe
from django.forms.models import model_to_dict
from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.core import validators
from django.conf import settings
from django.utils.deconstruct import deconstructible
from django.utils.timezone import localtime

from . import appname
from common import choices, help_texts

User = settings.AUTH_USER_MODEL

class Student(models.Model):

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('students:detail', kwargs={'pk':self.pk})

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    edit_time = models.DateTimeField('编辑时间',auto_now=True)

    xm=models.CharField('姓名', max_length=5, blank=True, help_text='请填写你的姓名', default='')
    xb=models.CharField('性别', max_length=1, blank=True, default='', choices=[('男', '男'), ('女', '女')])
    bj=models.CharField('班级', max_length=10, blank=True, help_text=help_texts.bj, default='', choices=choices.bj)
    cj=models.IntegerField('成绩', blank=True, help_text=help_texts.cj, default=0)