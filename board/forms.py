from django import forms
from django.utils.translation import ugettext as _
from django_summernote.widgets import SummernoteWidget
from datetime import datetime
from .models import *


class BoardEditForm(forms.ModelForm):
    """Form for board"""

    class Meta:
        """Meta for ModelForm"""

        CATEGORY = (
        )
        model = Board
        exclude = (
            'main_image', 'lang', 'custom_image',
        )
        widgets = {
            'status': forms.Select(choices=Board.BOARD_STATUS, attrs={'class': 'form-control'}),
            'category': forms.Select(choices=Category.objects.all(), attrs={'class': 'form-control'}),
            'title': forms.TextInput(
                attrs={'placeholder': _('제목을 입력하세요.'), 'class': 'form-control input-style'}
            ),

            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        """Init"""
        self.user = kwargs.pop('user', None)
        super(BoardEditForm, self).__init__(*args, **kwargs)
