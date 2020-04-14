from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    """Custom login form for suspension"""

    def confirm_login_allowed(self, user):
        """Override confirm_login_allowed"""
        if user.is_active:

            pass
        elif not user.is_active:
            error = "권한이 없습니다."
            raise forms.ValidationError(error, code='suspended')

