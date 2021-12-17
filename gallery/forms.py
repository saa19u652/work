from django import forms
from django.contrib.auth.models import User


class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})


class LoginForm(PlaceholderMixin, forms.Form):
    username = forms.CharField(required=True, label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    class Meta:
        model = User
        fields = ['username', 'password']
