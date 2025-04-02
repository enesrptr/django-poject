from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('anasayfa')

def iletisim(request):
    return HttpResponse('iletisim')

def hakkimizda(request):
    return HttpResponse('hakkimizda')
