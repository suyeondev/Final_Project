from django.urls import path
from mainAPP import views

urlpatterns = [
    path('index/',views.index, name='main'),

]
