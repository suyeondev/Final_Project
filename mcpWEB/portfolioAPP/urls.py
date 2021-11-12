from django.urls import path
from portfolioAPP import views

urlpatterns = [
    path('main/',views.index, name='main'),
    path('main/songinfo/',views.songInfo,name='songinfo'),
]
