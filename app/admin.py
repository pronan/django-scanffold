from django.contrib import admin
from .models import ${model_name}
# Register your models here.

class ${model_name}Admin(admin.ModelAdmin):
    pass
    
admin.site.register(${model_name}, ${model_name}Admin)