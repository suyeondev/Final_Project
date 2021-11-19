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
        per = [0.2,0.15,0.1,0.1,0.1,0.05,0.05]

        la_ss_per=[0.25,0.2,0.15,0.1,0.1,0.1,0.05,0.05]
        seed = []
        for i in per:
            seed_money = round(i * float(money))
            seed.append(seed_money)

        la_ss_seed = []
        for l in la_ss_per:
            lll = round(l * float(money))
            la_ss_seed.append(lll)
        context = {}
        short_safe=[]
        short_agg = []
        long_safe =[]
        long_agg =[]
        la_ss_per_txt=[25,20,15,10,10,10,5,5]
        per_txt = [20, 15, 10, 10, 10, 5, 5]
        first_seed = round(0.25 * float(money))
        last_seed =  round(0.05 * float(money))
        print('period : {}, propensity: {}, money : {}'.format(period, propensity, money))
        if (period == "short") & (propensity == "sta"):
            short_safe = SongInfo.objects.filter(Q(Q(cluster_bs=0) | Q(cluster_bs=1))&Q(price__lte = money)).order_by('-fee_near_year','-price')[:8]

        if (period == "short") & (propensity == "agg"):
            short_agg = SongInfo.objects.filter(Q(cluster_bs=2)&Q(price__lte = money)).order_by('price','-fee_near_year')[:7]

        if (period == "long") & (propensity == "sta"):
            long_safe = SongInfo.objects.filter(Q(Q(cluster_bl=0) | Q(cluster_bl=1))&Q(price__lte = money)).order_by('-fee_near_year','-price')[:7]

        if (period == "long") & (propensity == "agg"):
            long_agg = SongInfo.objects.filter(Q(cluster_bl=2)&Q(price__lte = money)).order_by('price','-fee_near_year')[:8]

        ss_zip = zip(short_safe,la_ss_per, la_ss_seed,la_ss_per_txt)
        sa_zip = zip(short_agg, per, seed,per_txt)
        ls_zip = zip(long_safe, per, seed,per_txt)
        la_zip = zip(long_agg, la_ss_per, la_ss_seed, la_ss_per_txt)

        context = {
            'period': period,
            'propensity': propensity,
            'money': money,
            'ss_zip': ss_zip,
            'sa_zip': sa_zip,
            'la_zip': la_zip,
            'ls_zip': ls_zip,
            'musics': musics,
            'first_seed':first_seed,
            'last_seed':last_seed,
        }
        # for ls, p, s in loop_zip :
        #     print(ls.title)
        #     print(p)
        #     print(s)
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