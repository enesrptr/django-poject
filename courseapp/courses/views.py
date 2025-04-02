from django.shortcuts import render
from django.http import HttpResponse

def kurslar(request):
    return HttpResponse('kurslar')

def kurslar_detay(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} kurs detaylari')

def getCoursesByCategory(request, category_name):

    return HttpResponse(category_name)


def getCoursesByCategoryId(request, category_id):
    return HttpResponse(category_id)

