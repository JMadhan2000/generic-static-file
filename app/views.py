from django.shortcuts import render

# Create your views here.
def madhan(request):
    return render(request,'madhan.html')

def madhan_name_spinning(request):
    return render(request,'madhan name spinning.html')

def animation(request):
    return render(request,'animation.html')

def sematic(request):
    return render(request,'sematic tags.html')

def media(request):
    return render(request,'media.html')

def rotate(request):
    return render(request,'rotate.html')

def landing_pages(request):
    return render(request,'landing pages.html')

def grid_system(request):
    return render(request,'grid system.html')

def indian_cricketres(request):
    return render(request,'indian cricketers.html')

def form(request):
    return render(request,'form.html')