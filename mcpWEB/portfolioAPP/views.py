from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('portfolioAPP index~~')
    return render(request, 'portfolio/dashboard.html')

def songInfo(request):
    print('portfolioAPP songinfo~~')
    return render(request, 'portfolio/songinfo.html')