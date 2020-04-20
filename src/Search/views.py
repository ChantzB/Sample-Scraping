from django.shortcuts import render
from . import forms
from .models import Samples

# Create your views here.
def index(request):
    form = forms.SampleForm()
    context = {'form' : form}
    if request.method == 'GET':
        form = forms.SampleForm(request.POST)
    else:
        form = forms.SampleForm()
    return render(request, 'search/search.htm', context)