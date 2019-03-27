from .models import Image,Profile
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments','likes','editor','user','profile' ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','profile' ]
