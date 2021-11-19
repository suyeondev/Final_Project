from django.urls import path
from portfolioAPP import views

urlpatterns = [
    path('main/', views.index, name='main'),
    path('main/songinfo/',views.songInfo,name='songinfo'),
    path('survey/',views.survey, name='survey'),
    path('main/predict/',views.predict, name='predict'),
    path('csvToModel/',views.csvToModel, name='csvToModel'), # csv파일을 모델생성 테스트페이지
]
