from django.shortcuts import render
from .models import Producers, Samples
from django.http import HttpResponse
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



# Create your views here.
def index(request):
    queryset = Producers.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'producers/producers.htm', context)


def bio(request, slug):
    producer = Producers.objects.get(slug = slug)
    queryset = Samples.objects.filter(producer=producer.producer_id)
    count = queryset.count()

    sample_contains_query = request.GET.get('artist_contains')
    
    if sample_contains_query != '' and sample_contains_query is not None:
        queryset = queryset.filter(Q(artist__icontains=sample_contains_query)
                                  | Q(title__icontains=sample_contains_query)
                                  ).distinct()
    paginator = Paginator(queryset, 15)
    page = request.GET.get('page')

    page_object = paginator.get_page(page)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
    'count' : count,
    'posts' : posts,
    'producer' : producer
    }
    
    return render(request, 'producers/bio.htm', context)


# def search(request, slug):
#     producer = Producers.objects.get(slug = slug)
#     queryset = Samples.objects.filter(producer=producer.producer_id)
#     count = queryset.count()

#     sample_contains_query = request.GET.get('artist_contains')
    
#     if sample_contains_query != '' and sample_contains_query is not None:
#         queryset = queryset.filter(Q(artist__icontains=sample_contains_query)
#                                   | Q(title__icontains=sample_contains_query)
#                                   ).distinct()
#     paginator = Paginator(queryset, 15)
#     page = request.GET.get('page')

#     page_object = paginator.get_page(page)

#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     context = {
#         'count' : count,
#         'posts' : posts,
#         'producer' : producer
#     }
    
#     return render(request, 'producers/search.htm', context)