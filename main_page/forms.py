from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

MAST_CHOICE=[('full','Full-stack developer'),('front','Frontend developer'),('back','Backend developer'),]

class ContactsForm(forms.Form):
    name = forms.CharField(max_length=32, min_length=3,)
    email = forms.EmailField()
    programming_lang = forms.CharField(max_length=128, min_length=1,)
    mast = forms.ChoiceField(choices=MAST_CHOICE)
