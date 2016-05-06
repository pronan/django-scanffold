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

class ${model_name}(models.Model):

    class Meta:
        verbose_name = "${verbose_name}"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('${app_name}:detail', kwargs={'pk':self.pk})

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    edit_time = models.DateTimeField('编辑时间',auto_now=True)

    ${model_fields}