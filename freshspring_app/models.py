from django.db import models
from django.utils.text import slugify

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
    content = models.TextField()
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
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
