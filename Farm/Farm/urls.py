from django.contrib import admin
from django.urls import path

from ranking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ranking/', views.ranking_detail, name='ranking'),
    path('about/', views.about, name='about')
]
