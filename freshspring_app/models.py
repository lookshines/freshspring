from django.db import models
from django.utils.text import slugify
#from ckeditor.fields import RichTextField
#from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import FileExtensionValidator

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services-images/', blank=True, null=True)
    icon = models.ImageField(upload_to='services-icons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Projects(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('borehole', 'Borehole'),
        ('domestic water treatment', 'Domestic Water Treatment'),
        ('industrial water treatment', 'Industrial Water Treatment'),
        ('consulting', 'Consulting'),
        ('others', 'Others'),
    ]
    
    project_title = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100, choices=PROJECT_TYPE_CHOICES)
    description = models.TextField(blank=True,null=True)
    project_display = models.ImageField(upload_to='project-display/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.project_title
    
class ProjectImages(models.Model):
    project = models.ForeignKey(Projects, related_name='images', on_delete=models.CASCADE)
    project_images = models.ImageField(upload_to='project-images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ContactMessages(models.Model):
    REQUEST_CHOICES = [
        ('borehole', 'Borehole'),
        ('domestic water treatment', 'Domestic Water Treatment'),
        ('industrial water treatment', 'Industrial Water Treatment'),
        ('consulting', 'Consulting'),
        ('general', 'General Enquiry'),
    ]
    
    fullname = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    request = models.CharField(max_length=100, choices= REQUEST_CHOICES)
    message = models.TextField()
    
    def __str__(self):
        return self.fullname

class Testimonial(models.Model):
    fullname = models.CharField(max_length=100)
    profession = models.CharField(max_length=50, blank=True, null=True)
    testimony = models.TextField()
    image = models.ImageField(upload_to='testimonial-images/', default='defaults/user-image-6.jpg', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize the image
        if self.image:
            image_path = self.image.path
            try:
                img = Image.open(image_path)
                img = img.convert('RGB')  # ensures PNGs are handled too
                img = img.resize((90, 90), Image.ANTIALIAS)
                img.save(image_path)
            except Exception as e:
                print(f"Image resize failed: {e}")

    def __str__(self):
        return self.fullname
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    content = CKEditor5Field('Text', config_name='default')
    image = models.ImageField(blank=True, null=True, upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PageSection(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Internal name for the section" )
    slug = models.SlugField(unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class StaticContent(models.Model):
    section = models.ForeignKey(PageSection, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    icon_text = models.CharField(max_length=100, blank=True, null=True)
    header = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.section}-{self.title}"
    
class ContactInformation(models.Model):
    title = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    whatsapp = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
class HomeBannerContent(models.Model):
    section = models.ForeignKey(PageSection, related_name='pagesectionbanner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    icon_text = models.CharField(max_length=100, blank=True, null=True)
    header = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=50, null=True)
    rating = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='home-banner-images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class TreatmentContent(models.Model):
    section = models.ForeignKey(PageSection, related_name='pagesectiontreatment', on_delete=models.CASCADE)
    serial = models.CharField(max_length=50, null=True, unique=True) 
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    icon = models.FileField(
        upload_to='treatment-icon/', 
        blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['svg'])]
        )

class About(models.Model):
    section = models.ForeignKey(PageSection, related_name='pagesectionabout', on_delete=models.CASCADE)
    quote = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    larger_image = models.ImageField(upload_to='about-image/',blank=True,null=True)
    smaller_image = models.ImageField(upload_to='about-image/',blank=True,null=True)

class AboutList(models.Model):
    about = models.ForeignKey(About, related_name='about', on_delete=models.CASCADE)
    list_item = models.CharField()
    
    def __str__(self):
        return self.list_item
    
class Value(models.Model):
    section = models.ForeignKey(PageSection, related_name='pagesectionvalue', on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    title =  models.CharField(max_length=50)
    content = models.TextField()
    
    def __str__(self):
        return self.position
    
class Feature(models.Model):
    section = models.ForeignKey(PageSection, related_name='pagesectionfeatures', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    
    def __str__(self):
        return self.item
    
class FunFact(models.Model):
    section = models.ForeignKey(PageSection, related_name='pagesectionfunfact', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    position = models.IntegerField(unique=True)
    paragraph = models.TextField()
    years = models.IntegerField()
    
    def __str__(self):
        return self.title