from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import *
import csv

# Create your views here.
def index(request):
    print('portfolioAPP index~~')
    # survey 페이지에서 데이터 받아오기
    if request.method == 'POST':
        period= request.POST.get('period')
        propensity= request.POST.get('propensity')
        money = request.POST.get('money')
        musics = SongInfo.objects.all()
        context = {
            'musics': musics,
            'period': period,
            'propensity': propensity,
            'money': money,
        }
        print('period : {}, propensity: {}, money : {}'.format(period, propensity, money))
        if (period == "short") & (propensity == "sta"):
            context['short_safe'] = SongInfo.objects.filter(Q(cluster_bs=0)|Q(cluster_bs=1)).order_by('-fee_near_year','-price')

        if (period == "short") & (propensity == "agg"):
            context['short_agg'] = SongInfo.objects.filter(Q(cluster_bs=2)).order_by('price','-fee_near_year')

        if (period == "long") & (propensity == "sta"):
            context['long_safe'] = SongInfo.objects.filter(Q(cluster_bl=0) | Q(cluster_bl=1)).order_by('-fee_near_year','-price')

        if (period == "long") & (propensity == "agg"):
            context['long_agg'] = SongInfo.objects.filter(Q(cluster_bl=2)).order_by('price','-fee_near_year')

    return render(request, 'portfolio/dashboard.html',context)

def songInfo(request):
    print('portfolioAPP songinfo~~')
    return render(request, 'portfolio/songinfo.html')

def survey(request):
    print('mainAPP survey')
    return render(request, 'portfolio/survey.html')

def csvToModel(request):
    path='C:/Users/whgud/TIL/team project/music_final.csv'
    file=open(path, encoding='UTF8')
    reader = csv.reader(file)
    print('reader----------',reader)
    csvList=[]
    for row in reader:
        print('row------',row)
        csvList.append(SongInfo(title=row[0],
                               artist=row[1],
                               price=row[2],
                               fee_near_year=row[6],
                               album=row[8],
                               genre=row[9],
                               publisher=row[10],
                               cluster_a=row[19],
                               cluster_bs=row[20],
                               cluster_bl=row[21],
                               img_url_txt=row[22],
                               img_url=row[22],
                               writer=row[23],
                               composer=row[24],
                               pub_date=row[25]
                              ))
    SongInfo.objects.bulk_create(csvList)
    return HttpResponse('create model ok')