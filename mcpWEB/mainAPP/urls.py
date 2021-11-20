from django.urls import path
from mainAPP import views

urlpatterns = [
    path('index/',views.index, name='main'),
    path('index/about3m/', views.about, name='about')
]
