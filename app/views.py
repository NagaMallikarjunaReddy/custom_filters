from django.shortcuts import render

# Create your views here.
def sample(request):
    d={'data':'ThIs Is DjAnGo class'}
    return render(request,'filter.html',d)