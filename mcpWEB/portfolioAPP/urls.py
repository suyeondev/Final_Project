from django.urls import path
from portfolioAPP import views

urlpatterns = [
    path('main/', views.index, name='main'), # 포트폴리오 화면 보여줄 페이지
    path('main/songinfo/',views.songInfo,name='songinfo'), # 곡정보 보여줄 페이지
    path('main/songinfo_icant/', views.songInfoIcant, name='songinfo_icant'),
    path('survey/',views.survey, name='survey'), # 설문조사 , 사용자 정보 받아올 페이지
    path('main/predict/',views.predict, name='predict'), # 예측화면 보여줄 페이지
    path('main/predict_icant/',views.predictIcant, name='predict_icant'),
    path('csvToModel/',views.csvToModel, name='csvToModel'), # csv파일을 모델생성 테스트페이지
]
