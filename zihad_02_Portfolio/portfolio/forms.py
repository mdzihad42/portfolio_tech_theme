from django import forms
from .models import Hero, About, Skill, Project, Experience, Education, BlogCategory, BlogPost

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = '__all__'
        widgets = {
            'short_intro': forms.Textarea(attrs={'rows': 3}),
        }

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'long_bio': forms.Textarea(attrs={'rows': 5}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'responsibilities': forms.Textarea(attrs={'rows': 4}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 8}),
        }
