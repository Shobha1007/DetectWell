from django.shortcuts import render
from .models import places
# Create your views here.
def index(request):
    
    place = places.objects.all()

    return render(request,'index.html',{'place': place})
