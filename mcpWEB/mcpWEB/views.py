from django.shortcuts import  render
from django.http import HttpResponse

def index(request):
    print('mainpage index~~')
    return render(request, 'index.html')