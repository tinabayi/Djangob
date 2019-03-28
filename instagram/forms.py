from .models import Image,Profile,Comment
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments','likes','editor','user','profile' ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','last_name' ]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image' ]
