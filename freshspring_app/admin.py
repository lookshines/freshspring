from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
#from .forms import UserRegistrationForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from django import forms

# Register your models here.
admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(ProjectImages)
admin.site.register(ContactMessages)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Comment)

class SectionInline(admin.TabularInline):
    model = StaticContent
    extra = 1

class PageSectionAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    prepopulated_fields = {'slug': ('name',)}
    
class StaticContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_text','header')
    
admin.site.register(PageSection, PageSectionAdmin)

admin.site.register(StaticContent, StaticContentAdmin)

@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('title','phone', 'whatsapp','email')
    
@admin.register(HomeBannerContent)
class HomeBannerContentAdmin(admin.ModelAdmin):
    list_display = ('title','icon_text', 'header')
    
@admin.register(TreatmentContent)
class TreatmentContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'icon')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('quote', 'name', 'role', 'content')

admin.site.register(AboutList)
    
admin.site.register(Value)
admin.site.register(Feature)
admin.site.register(FunFact)

# Change the site header (top left corner text)
#admin.site.site_header = "FreshSpring Admin"

# Change the title that appears on the browser tab
admin.site.site_title = "FreshSpring Admin Portal"

# Change the index page title
admin.site.index_title = "Welcome to FreshSpring Administration"

class UserRegistrationForm(forms.ModelForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-select form-control'}),
        label='Group',
        help_text='Select the group for the user.'
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'group', 'is_staff', 'is_active')
        
    def save(self, commit=True):
        user =super().save(commit=False)
        
        # ✅ make password unusable (user must reset it)
        user.set_unusable_password()  # Set an unusable password initially
        
        if commit:
            user.save()
            # ensure only one group is set
            user.groups.clear()
            user.groups.add(self.cleaned_data['group'])
        return user
    
class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'group', 'is_staff', 'is_active')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # If creating a new user
            group = form.cleaned_data.get('group')
            if group:
                obj.groups.clear()
                obj.groups.add(group)
            
            # send password setup link
            self.send_password_setup_link(request, obj)
        
        else:
            # If updating an existing user, ensure groups are updated
            if 'group' in form.cleaned_data:
                obj.groups.set(form.cleaned_data['group'])                     
            
    def send_password_setup_link(self, request, user):
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        password_reset_url = f"{request.scheme}://{request.get_host()}/reset/{uid}/{token}/"
        
        send_mail(
            subject="Set Your Password",
            message = (
            f"Hello {user.username},\n\n"
            f"An account has been created for you. Please set your password by clicking the link below:\n"
            f"{password_reset_url}\n\n"
            f"If you did not expect this email, you can ignore it."
        ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
# Re-register User with custom admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
            