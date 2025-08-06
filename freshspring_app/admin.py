from django.contrib import admin
from .models import Services, Projects, ProjectImages, ContactMessages, Testimonial, Blog, Comment

# Register your models here.
admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(ProjectImages)
admin.site.register(ContactMessages)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Comment)