from django.shortcuts import render
from django.http import HttpResponse

def kurslar(request):
    return HttpResponse('kurslar')

def kurslar_detay(request):
    return HttpResponse('kurs detaylari')



