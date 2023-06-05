from django.shortcuts import render
from .forms import Selling

from .models import Photo
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

def selling(request,msg):
    fsa = Photo.objects.get(pk=msg)
    if request.method == 'POST':
        fm = Selling(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['first_name']
            fm.save()
            return render(request,'watch/newform.html',{'image':fsa,'name':name})

    else:
        fm = Selling()
    return render(request,'watch/selling.html',{'forms':fm})

