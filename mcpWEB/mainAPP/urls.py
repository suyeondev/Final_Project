from django.urls import path
from mainAPP import views

urlpatterns = [
    path('main/',views.index, name='main'),

]
