# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from.models import *
from django.core.cache import cache
from django.conf import settings
from django_cache.settings import cache_time_out
from django.core.cache.backends.base import DEFAULT_TIMEOUT

#CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# Create your views here.



# Create your views here.

@api_view(['GET'])
def view_books(request):
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def view_cached_books(request):
    if 'product' in cache:
        print "cache pro"
        # get results from cache
        products = cache.get('product')
        return Response(products, status=status.HTTP_201_CREATED)

    else:
        print "here "
        products = Product.objects.all()
        results = [product.to_json() for product in products]
        # store data in cache
        ls = cache.set('product', results, timeout=cache_time_out)
        print ls
        return Response(results, status=status.HTTP_201_CREATED)