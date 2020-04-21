from django import forms
from .models import Samples, Producers

# class SampleForm(forms.ModelForm):
#     class Meta:
#         model = Samples
#         fields = ['song_id', 'artist', 'title']
#         widgets = {
#             'artist' : forms.TextInput(
#             attrs={'class' : 'form-control', 'name' : 'artist', 'placeholder' : 'Artist'}),
#             'title' : forms.TextInput(
#             attrs={'class' : 'form-control', 'name' : 'title', 'placeholder' : 'Title'})
#         }
        