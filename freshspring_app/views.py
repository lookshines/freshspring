from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'freshspring_app/index.html')

def services(request):
    return render(request, 'freshspring_app/services.html')

def portfolio(request):
    return render(request, 'freshspring_app/portfolio.html')

def blog(request):
    return render(request, 'freshspring_app/blog.html')

def contact(request):
    return render(request, 'freshspring_app/contact.html')