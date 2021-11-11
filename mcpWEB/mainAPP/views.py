from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('mainAPP index~~')
    return render(request, 'main/main.html')

def contact(request):
    print('mainAPP contact')
    return render(request, 'main/contact.html')
# Create your views here.
