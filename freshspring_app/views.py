from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.db.models import Prefetch
from .forms import ContactForm, CommentForm

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
        form1 = ContactForm()
        return form1, True
    return form, False
        

def index(request):
    services = Services.objects.all().order_by('-created_at')[:5]
    projects = Projects.objects.all()
    project_images = ProjectImages.objects.all()
    testimonials = Testimonial.objects.all().order_by('-created_at')[:3]
    blogs = Blog.objects.all().order_by('created_at')[:3].prefetch_related()
    form, success = handle_contact_form(request)
    contact = ContactInformation.objects.order_by('-id').first()
    
    phone = contact.phone if contact else ''
    whatsapp = contact.whatsapp if contact else ''
    
    formated_phone = f"{phone[:3]} ({phone[3:6]}) {phone[6:9]} {phone[-4:]}" if phone else ''
    formated_whatsapp = f"{whatsapp[:3]} ({whatsapp[3:6]}) {phone[6:9]} {phone[-4:]}" if whatsapp else ''
    
    page_sections = PageSection.objects.prefetch_related(
        'sections',
        'pagesectionbanner',
        'pagesectiontreatment',
        Prefetch(
            'pagesectionabout',
            queryset=About.objects.order_by('-id').prefetch_related('about')
        ),
        'pagesectionvalue',
        'pagesectionfeatures',
        'pagesectionfunfact'
    )
    
    features = []
    for section in page_sections:
        if section.slug == 'about':
            latest_about = section.pagesectionabout.all().first()
            features.extend(latest_about.about.all())
            
    half = len(features) // 2 + len(features) % 2
    col1 = features[:half]
    col2 = features[half:]
    
    context = {
        'services': services,
        'projects': projects,
        'project_images': project_images,
        'form': form,
        'testimonials': testimonials,
        'blogs': blogs,
        'page_sections': page_sections,
        'col1':col1,
        'col2':col2,
        'contact': contact,
        'formated_phone': formated_phone,
        'formated_whatsapp': formated_whatsapp,
    }    
    return render(request, 'freshspring_app/index.html', context)

def services(request):
    services = Services.objects.all()
    page_sections = PageSection.objects.prefetch_related(
        'sections',
        'pagesectionvalue'
    )
    contact = ContactInformation.objects.order_by('-id').first()
    
    
    context = {
        'services': services,
        'page_sections': page_sections,
        'contact': contact,
    }
    
    return render(request, 'freshspring_app/services.html', context)

def portfolio(request):
    page_sections = PageSection.objects.prefetch_related(
        'sections',
        'pagesectiontreatment'
    )
    projects = Projects.objects.all()
    
    context = {
        'page_sections': page_sections,
        'projects': projects
    }
    return render(request, 'freshspring_app/portfolio.html',context)

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
    contact = ContactInformation.objects.order_by('-id').first()
    
    phone = contact.phone if contact else ''
    whatsapp = contact.whatsapp if contact else ''
    
    formated_phone = f"{phone[:3]} ({phone[3:6]}) {phone[6:9]} {phone[-4:]}" if phone else ''
    formated_whatsapp = f"{whatsapp[:3]} ({whatsapp[3:6]}) {phone[6:9]} {phone[-4:]}" if whatsapp else ''   
    
    context = {
        'form': form,
        'contact': contact,
        'formated_phone': formated_phone,
        'formated_whatsapp': formated_whatsapp,
    }
    
    return render(request, 'freshspring_app/contact.html', context)

def blog_detail(request, slug):
    blogs = Blog.objects.all().order_by('created_at')
    post = get_object_or_404(Blog, slug=slug)
    comments = post.comments.all()
    services= Services.objects.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)   # don’t save yet
            comment.blog = post                # attach blog
            comment.save()
            return redirect('blog_detail', slug=slug)
        
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'services': services,
        'blogs': blogs,
        'form': form
    } 
    return render(request, 'freshspring_app/blog_details.html', context)