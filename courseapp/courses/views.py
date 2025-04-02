from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

data = {
    "programlama" : "programlama kategorisine ait kurslar",
    "web-gelistirme" : "web-gelistirme kategorisine ait kurslar"
}

def kurslar(request):
    return HttpResponse('kurslar')

def kurslar_detay(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} kurs detaylari')


def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlis kategori secimi ")


def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id <= 0 or category_id > len(category_list):
        return HttpResponseNotFound("Yanlis kategori secimi")
    

    category_name = category_list[category_id - 1]

    redirect_url = reverse("courses_by_category", args=[category_name])
    
    return redirect (redirect_url)

