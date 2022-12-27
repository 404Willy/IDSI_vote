from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class FormulaireEnregistrement(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        