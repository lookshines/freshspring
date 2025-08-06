from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .models import Services, Projects, ProjectImages, Testimonial, Blog, Comment
from .forms import ContactForm

# Create your views here.

def handle_contact_form(request):
    """
    Handles contact form processing and email sending.
    Returns a tuple: (form instance, success boolean)
    """
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        message = form.save()
        
        # Send email notification
        send_mail(
            subject=f"New Contact Message from {message.fullname}",
            message=(
                f"Name: {message.fullname}\n"
                f"Email: {message.email}\n"
                f"Phone: {message.phone}\n"
                f"Request: {message.request}\n"
                f"Message: {message.message}"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['damolamewojuaye@gmail.com'],  # Change this
            fail_silently=False,
        )
        messages.success(request, "Thank you! Your message has been sent successfully.")
        return form, True
    return form, False
        

def index(request):
    services = Services.objects.all().order_by('-created_at')[:5]
    projects = Projects.objects.all()
    project_images = ProjectImages.objects.all()
    testimonials = Testimonial.objects.all().order_by('-created_at')[:3]
    blogs = Blog.objects.all().order_by('created_at')[:3].prefetch_related()
    
    form, success = handle_contact_form(request)
    if success:
        return redirect('home')
    
    context = {
        'services': services,
        'projects': projects,
        'project_images': project_images,
        'form': form,
        'testimonials': testimonials,
        'blogs': blogs
    }    
    return render(request, 'freshspring_app/index.html', context)

def services(request):
    services = Services.objects.all()
    return render(request, 'freshspring_app/services.html', {'services': services})

def portfolio(request):
    projects = Projects.objects.all()
    return render(request, 'freshspring_app/portfolio.html',{'projects': projects})

def blog(request):
    blogs = Blog.objects.all().order_by('created_at')
    paginator = Paginator(blogs, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    services = Services.objects.all().prefetch_related()
    
    context = {
        'blogs': page_obj,
        'services': services
    }
    return render(request, 'freshspring_app/blog.html', context)

def contact(request):
    form, success = handle_contact_form(request)
    if success:
        return redirect('home')
    
    return render(request, 'freshspring_app/contact.html', {'form': form})

def blog_detail(request, slug):
    blogs = Blog.objects.all().order_by('created_at')
    post = get_object_or_404(Blog, slug=slug)
    comments = post.comments.all()
    services= Services.objects.all()
    context = {
        'post': post,
        'comments': comments,
        'services': services,
        'blogs': blogs
    } 
    return render(request, 'freshspring_app/blog_details.html', context)