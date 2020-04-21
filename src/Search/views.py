from django.shortcuts import render
from django.db.models import Q
from . import forms
from .models import Samples

# Create your views here.
def index(request):
    queryset = Samples.objects.all()
    sample_contains_query = request.GET.get('sample_contains')

    if sample_contains_query != '' and sample_contains_query is not None:
        queryset = queryset.filter(Q(artist__icontains=sample_contains_query)
                                  | Q(title__icontains=sample_contains_query)
                                  ).distinct()
    context = {
        'queryset': queryset
    }
    
    return render(request, 'search/homepage.htm', context)