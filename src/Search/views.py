from django.shortcuts import render
from django.db.models import Q
from . import forms
from .models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    queryset = Articles.objects.all()
    

    context = {
        'queryset' : queryset
    }
    
    return render(request, 'search/homepage.htm', context)