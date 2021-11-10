from django.urls import path
from portfolioAPP import views

urlpatterns = [
    path('main/',views.index, name='main'),
    path('table/',views.table,name='table'),
]
