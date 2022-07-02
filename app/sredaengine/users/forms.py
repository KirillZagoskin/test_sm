from dataclasses import fields
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm


User = get_user_model()


class SignUpForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = ()
        field_classes = {}
