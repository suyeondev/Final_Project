from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import csv

# Create your views here.
def index(request):
    print('portfolioAPP index~~')
    return render(request, 'portfolio/dashboard.html')

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
        csvList.append(Musics(title=row[0],
                               artist=row[1],
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
                               pub_date=[25]
                              ))
    Musics.objects.bulk_create(csvList)
    return HttpResponse('create model ok')