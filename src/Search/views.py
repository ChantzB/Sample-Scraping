from django.shortcuts import render
from django.db.models import Q
from . import forms
from .models import Articles, Highlights
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    queryset = Articles.objects.all()
    highlights = Highlights.objects.all()
    # if highlights.count() > 0:
    #     highlights = highlights[0:4]
    # else:
    #     return None

    context = {
        'queryset' : queryset,
        'highlights' : highlights
    }
    
    return render(request, 'search/homepage.htm', context)