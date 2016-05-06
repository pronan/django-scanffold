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

class ${form_name}(forms.ModelForm):

    class Meta:
        model = models.${model_name}
        fields = ${form_fields}

        error_messages = {
            ${form_error_messages}
        }
        widgets = {
            ${form_widgets}
        }
        labels = {
            ${form_labels}      
        }

    # def __init__(self, *arg,**kwargs):
    #     super().__init__(*arg, **kwargs)