from django.shortcuts import render
from django.db.models import Q
from . import forms
from .models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):


    context = {
    }
    
    return render(request, 'search/homepage.htm', context)