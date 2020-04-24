from django.shortcuts import render
from .models import Producers
from django.http import HttpResponse

# Create your views here.
def index(request):
    queryset = Producers.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'producers/producers.htm', context)

def bio(request, slug):
    producer = Producers.objects.get(slug=slug)
    context = {
        'producer' : producer
    }
    return render(request, 'producers/bio.htm', context)