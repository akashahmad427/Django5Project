from django.shortcuts import render
from .forms import Storedata
# Create your views here.
def home(request):
    return render(request,'watch/home.html')


def more(request):
    return render(request,'watch/morepic.html')
    
def perchar(request):
    fm = Storedata()
    return render(request,'watch/form.html',{'form':fm})
