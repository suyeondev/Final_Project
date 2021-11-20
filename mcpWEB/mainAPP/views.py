from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('mainAPP index~~')
    return render(request, 'main/main.html')


def about(request):
    print('mainAPP about3m~~')
    return render(request, 'main/about3m.html')

# Create your views here.
