from django.shortcuts import render
from .models import Services

# Create your views here.
def index(request):
    services = Services.objects.all()
    return render(request, 'freshspring_app/index.html', {'services': services})

def services(request):
    services = Services.objects.all()
    return render(request, 'freshspring_app/services.html', {'services': services})

def portfolio(request):
    return render(request, 'freshspring_app/portfolio.html')

def blog(request):
    return render(request, 'freshspring_app/blog.html')

def contact(request):
    return render(request, 'freshspring_app/contact.html')