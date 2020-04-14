from django.contrib import admin
from .models import *

@admin.register(Whitepaper)
class LangTypeAD(admin.ModelAdmin):
    list_display = ['lang_type', 'files', 'is_open']