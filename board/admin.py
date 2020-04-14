from django.contrib import admin
from .models import *



@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'lang', 'category', 'status', 'created_at']
    list_filter = ['status', 'lang']
    search_fields = ["title"]

@admin.register(LangType)
class LangTypeAD(admin.ModelAdmin):
    list_display = ['lang_type']

@admin.register(Category)
class CategoryAD(admin.ModelAdmin):
    list_display = ['category']