from django.shortcuts import render
from .models import Producers

# Create your views here.
def index(request):
    queryset = Producers.objects.all()
    context = {
        'queryset': queryset
    }
    
    return render(request, 'producers/producers.htm', context)