from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('portfolioAPP index~~')
    return render(request, 'portfolio/dashboard.html')

def table(request):
    print('portfolioAPP table')
    return render(request, 'portfolio/tables.html')