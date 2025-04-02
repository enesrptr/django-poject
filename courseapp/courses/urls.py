from django.urls import path
from . import views



urlpatterns = [
    path('list',views.kurslar),
    path('details',views.kurslar_detay),
]
