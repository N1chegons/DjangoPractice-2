from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index , name='main'),
    path('instr/', views.instr, name='instr'),
    path('about/', views.about, name='about'),
    path('sum/', views.sum, name='sum'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

