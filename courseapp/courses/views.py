from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from datetime import date,datetime

data = {
    "programlama" : "programlama kategorisine ait kurslar",
    "web-gelistirme" : "web-gelistirme kategorisine ait kurslar",
    "mobil" : "mobil kategorisine ait kurslar",

}

db = {
    "courses": [
        {
            "title" : "javascript kursu",
            "description" : "javascript kurs aciklamasi",
            "imageUrl" : "1.jpg",
            "slug" : "java-script-kursu",
            "date" : datetime.now(),
            "isActive" : True,
            "isUpdated": False
        },

        {
            "title" : "python kursu",
            "description" : "python kurs aciklamasi",
            "imageUrl" : "2.jpg",
            "slug" : "python-kursu",
            "date" : date(2025,9,10),
            "isActive" : False,
            "isUpdated": False

        },

        {
            "title" : "web gelistirme kursu",
            "description" : "web gelistirme kurs aciklamasi",
            "imageUrl" : "3.jpg",
            "slug" : "web-gelistirme-kursu",
            "date" : date(2025,8,10),
            "isActive" : True,
            "isUpdated": True

        }
    ],
    "categories" : [
        {"id":1 ,"name": "programlama","slug":"programlama"},
        {"id":2 ,"name": "web gelistirme","slug":"web-gelistirme"},
        {"id":3 ,"name": "mobil uygulamalar","slug":"mobil-uygulamalar"}    
    ]
}

def index(request):

    kurslar = [course for course in db["courses"] if course["isActive"]==True]
    kategoriler = db["categories"]


    return render(request,'courses/index.html',{
        'categories' : kategoriler,
        'courses' : kurslar
    })

def kurslar_detay(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} kurs detaylari')


def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'courses/kurslar.html',{
            'category' : category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("yanlis kategori secimi ")


def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id <= 0 or category_id > len(category_list):
        return HttpResponseNotFound("Yanlis kategori secimi")
    

    category_name = category_list[category_id - 1]

    redirect_url = reverse("courses_by_category", args=[category_name])
    
    return redirect (redirect_url)

