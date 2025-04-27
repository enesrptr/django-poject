from django.urls import path
from . import views



urlpatterns = [
    path('',views.index, name="index"),
    path('search',views.search, name="search"), #give a name to reach search and use it navbar
    path('create-course',views.create_course, name="create_course"), #give a name to reach search and use it navbar
    path('course-list',views.course_list, name = "course_list"),
    path('course-edit/<int:id>',views.course_edit,name = "course_edit"),
    path('upload',views.upload,name = "upload_image"),
    path('course-delete/<int:id>',views.course_delete,name = "course_delete"),
    path('<slug:slug>',views.details, name = "course_details"),
    path('category/<slug:slug>',views.getCoursesByCategory, name='courses_by_category'),
]
