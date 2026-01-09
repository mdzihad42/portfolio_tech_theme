from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Custom Admin URLs
    path('dashboard/manage/<str:model_name>/', views.custom_admin_list, name='custom_admin_list'),
    path('dashboard/manage/<str:model_name>/add/', views.custom_admin_create, name='custom_admin_create'),
    path('dashboard/manage/<str:model_name>/edit/<int:pk>/', views.custom_admin_update, name='custom_admin_update'),
    path('dashboard/manage/<str:model_name>/delete/<int:pk>/', views.custom_admin_delete, name='custom_admin_delete'),
]
