import re
import os
from jinja2 import Template
from datetime import date
from collections import OrderedDict

from django.utils.safestring import mark_safe
from django.forms.widgets import ClearableFileInput
from django.forms.models import model_to_dict
from django.forms.fields import ImageField
from django.core.validators import BaseValidator
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError,ImproperlyConfigured
from django import forms

from . import models
from common import choices, help_texts

cd = os.path.dirname(__file__)

class Student(forms.ModelForm):

    class Meta:
        model = models.Student
        fields = ['xm', 'xb', 'bj', 'cj']

        error_messages = {
            # 'xm':{"":""},
            # 'xb':{"":""},
            # 'bj':{"":""},
            # 'cj':{"":""},
        }
        widgets = {
            'xm':forms.TextInput(attrs={'placeholder':'请填写你的姓名','title':'请填写你的姓名'}),
            'cj':forms.TextInput(attrs={'placeholder':help_texts.cj,'title':help_texts.cj}),
        }
        labels = {
            'xm':'姓名',
            'xb':'性别',
            'bj':'班级',
            'cj':'成绩',      
        }

    # def __init__(self, *arg,**kwargs):
    #     super().__init__(*arg, **kwargs)