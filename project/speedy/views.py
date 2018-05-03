from django.shortcuts import render
from django.http import HttpResponse
from .models import Speedy

# Create your views here.
def home(request):
    speedies=Speedy.objects.all()
    speedies_names=list()

    for speedy in speedies:
        speedies_names.append(speedy.name)

    response_html='<br>'.join(speedies_names)    
    return HttpResponse(response_html)
    return render(request,'home.html', {'speedies':speedies})