"""planwayIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.AdminHome.as_view(), name='home'),
    path('service/', views.Service.as_view(), name='service'),
    path('about/', views.about.as_view(), name='about'),
    path('portfolio/', views.portfolio.as_view(), name='portfolio'),
    path('team/', views.team.as_view(), name='team'),
    path('contact/', views.contact, name='contact'),
    path('team-augmentation/', views.TeamAugmentation, name='team_augmentation'),
    path('fixed-price-projects/', views.FixedPriceProjects, name='fixed_price_projects'),
    path('project-consulting/', views.ProjectConsulting, name='project_consulting'),
    path('support-maintenance/', views.SupportMaintenance, name='support_maintenance'),
    path('custom-software-developmet/', views.CustomSoftwareDevelopment, name='custom_software_development'),


    path('azure-aws/', views.AzureAws, name='azure_aws'),
    path('data-science/', views.DataScience, name='data_science'),
    path('dev-ops/', views.DevOps, name='dev_ops'),
    path('mobile-application-development/', views.MobileAppDevelopment, name='mobile_application_development'),
    path('sqa-training/', views.SQATrainging, name='sqa_training'),
    path('ui-ux-design/', views.UiUxDesign, name='ui_ux_design'),
    path('web-application-development/', views.WebApplicationDevelopment, name='web_application_development'),

]
