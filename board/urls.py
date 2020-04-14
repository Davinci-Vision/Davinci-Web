from django.urls import path
from .views import *
from .crud_board import *

urlpatterns = [
    path('', show_list, name="show_list"),
    path('new/', new_article, name="new_article"),

    path('article/<int:id>/', show_article, name="show_article"),

    path('edit/<int:id>/', edit_article, name="edit_article"),
    path('delete/<int:id>/', delete_article, name="delete_article", kwargs={'stay': False}),

]
