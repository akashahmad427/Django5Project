from django.shortcuts import render
from .forms import Selling
# Create your views here.
def home(request):
    
    return render(request,'watch/home.html')


def more(request):
    return render(request,'watch/morepic.html')
    
def perchar(request):
    fm = Selling()
    return render(request,'watch/form.html',{'form':fm})

def contact(request):
    return render(request,'watch/form.html')

def about(request):
    return render(request,'watch/about.html')

def selling(request):
    fm = Selling()
    return render(request,'watch/selling.html',{'forms':fm})

def test(request):
    fm = Selling
    return render(request,'watch/morewatch.html',{'forms':fm})