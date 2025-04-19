from django.urls import path
from . import views



urlpatterns = [
    path('',views.index, name="index"),
    path('search',views.search, name="search"), #give a name to reach search and use it navbar
    path('<slug:slug>',views.details, name = "course_details"),
    path('category/<slug:slug>',views.getCoursesByCategory, name='courses_by_category'),
]
