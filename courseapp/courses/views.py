from django.shortcuts import get_object_or_404, redirect, render

from courses.forms import CourseCreateForm
from .models import Course,Category
from django.core.paginator import Paginator

def index(request):

    kurslar = Course.objects.filter(isActive = 1, isHome = 1)
    kategoriler = Category.objects.all()


    return render(request,'courses/index.html',{
        'categories' : kategoriler,
        'courses' : kurslar
    })

def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)

        if form.is_valid():
            kurs = Course(title = form.cleaned_data["title"], 
                          description = form.cleaned_data["description"], 
                          imageUrl = form.cleaned_data["imageUrl"],
                          slug = form.cleaned_data["slug"])
            kurs.save()
            return redirect('/kurslar')
    else:
        form = CourseCreateForm()
        
    return render(request, "courses/create-course.html", {"form": form})


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=1, title__contains = q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar")

    return render(request, 'courses/search.html', {
        'categories': kategoriler,
        'courses': kurslar,
    })



def details(request, slug):

    # try:
    #     course = Course.objects.get(pk=kurs_id)
    # except:
    #     raise Http404()

    course = get_object_or_404(Course, slug=slug)
    
    context = {
        'course':course
    }
    return render(request,'courses/details.html',context)


def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=1).order_by("date")
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    return render(request, 'courses/list.html', {
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug
    })



