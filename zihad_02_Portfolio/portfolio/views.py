from django.shortcuts import render, get_object_or_404
from .models import Hero, About, Skill, Project, Experience, Education, Contact, BlogPost, BlogCategory
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json

def home(request):
    hero = Hero.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()[:6]  # Show latest 6 projects
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    context = {
        'hero': hero,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {'about': about})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'portfolio/experience.html', {'experiences': experiences})

def education(request):
    educations = Education.objects.all()
    return render(request, 'portfolio/education.html', {'educations': educations})

def blog(request):
    category_id = request.GET.get('category')
    if category_id:
        posts = BlogPost.objects.filter(category_id=category_id)
    else:
        posts = BlogPost.objects.all()
    categories = BlogCategory.objects.all()
    return render(request, 'portfolio/blog.html', {'posts': posts, 'categories': categories})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print("contact worked")

        # Save to database
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        # Send email notification
        try:
            email_subject = f"New Contact Form Message: {subject}"
            email_message = f"""
New message from your portfolio website:

From: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
This message was sent from your portfolio contact form.
"""
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,
                [settings.DEFAULT_FROM_EMAIL],  # Send to yourself
                fail_silently=False,
            )
            print("mail send: ",)
        except Exception as e:
            # Log the error but don't fail the request
            print(f"Email sending failed: {e}")

        return JsonResponse({'success': True})
        return JsonResponse({'success': True})
    return render(request, 'portfolio/contact.html')

from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    context = {
        'hero_count': Hero.objects.count(),
        'project_count': Project.objects.count(),
        'skill_count': Skill.objects.count(),
        'experience_count': Experience.objects.count(),
        'education_count': Education.objects.count(),
        'blog_count': BlogPost.objects.count(),
        'contact_count': Contact.objects.count(),
    }
    return render(request, 'portfolio/dashboard.html', context)

# --- Custom Admin Views ---
from django.shortcuts import redirect
from .forms import HeroForm, AboutForm, SkillForm, ProjectForm, ExperienceForm, EducationForm, BlogPostForm

# Configuration to map string names to Model and Form classes
MODEL_MAPPING = {
    'hero': {'model': Hero, 'form': HeroForm},
    'about': {'model': About, 'form': AboutForm},
    'skill': {'model': Skill, 'form': SkillForm},
    'project': {'model': Project, 'form': ProjectForm},
    'experience': {'model': Experience, 'form': ExperienceForm},
    'education': {'model': Education, 'form': EducationForm},
    'blogpost': {'model': BlogPost, 'form': BlogPostForm},
    'contact': {'model': Contact, 'form': None}, # Contact is usually read-only
}

def get_model_config(model_name):
    """Helper to get model class and form class from string name"""
    return MODEL_MAPPING.get(model_name.lower())

@login_required
@user_passes_test(lambda u: u.is_staff)
def custom_admin_list(request, model_name):
    config = get_model_config(model_name)
    if not config:
        return redirect('dashboard')
    
    items = config['model'].objects.all()
    context = {
        'items': items,
        'model_name': model_name,
    }
    return render(request, 'portfolio/admin_list.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def custom_admin_create(request, model_name):
    config = get_model_config(model_name)
    if not config or not config['form']:
        return redirect('custom_admin_list', model_name=model_name)
    
    if request.method == 'POST':
        form = config['form'](request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_list', model_name=model_name)
    else:
        form = config['form']()
    
    context = {
        'form': form,
        'model_name': model_name,
        'action': 'Add'
    }
    return render(request, 'portfolio/admin_form.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def custom_admin_update(request, model_name, pk):
    config = get_model_config(model_name)
    if not config or not config['form']:
        return redirect('custom_admin_list', model_name=model_name)
    
    item = get_object_or_404(config['model'], pk=pk)
    
    if request.method == 'POST':
        form = config['form'](request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_list', model_name=model_name)
    else:
        form = config['form'](instance=item)
    
    context = {
        'form': form,
        'model_name': model_name,
        'action': 'Edit'
    }
    return render(request, 'portfolio/admin_form.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def custom_admin_delete(request, model_name, pk):
    config = get_model_config(model_name)
    if not config:
        return redirect('dashboard')
    
    item = get_object_or_404(config['model'], pk=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('custom_admin_list', model_name=model_name)
    
    context = {
        'item': item,
        'model_name': model_name
    }
    return render(request, 'portfolio/admin_confirm_delete.html', context)
