
from django.shortcuts import render
from .models import Service

def index(request):
    services = Service.objects.filter(active=True).order_by('order')
    context = {
        'services': services
    }
    return render(request, 'myapp/index.html', context)