from django.shortcuts import render
from django.views.generic.base import View
from datetime import datetime
from django.db.models import Count, Sum, Avg
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.template.loader import get_template
from django.views import View
from django.core.mail import send_mail
from sadmin.models import OfficialContactInformation, TeamMambarProfile, Contact, Clients, PortfolioImage,CaseStudy


# Create your views here.
# @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)


class AdminHome(View):

    def get(self, request):
        get_all_testimonials = Clients.objects.all()[::-1]

        context = {
            "testimonials":get_all_testimonials,
            "isact_home": "active"

        }
        return render(request, "index.html", context)


class Service(View):

    def get(self, request):
        context = {
            "isact_service": "active"
        }
        return render(request, "service-details.html", context)


class about(View):

    def get(self, request):
        context = {
            "isact_about": "active"
        }
        return render(request, "about.html", context)

class pricing(View):

    def get(self, request):
        context = {
            "isact_about": "active"
        }
        return render(request, "pricing.html", context)



class team(View):

    def get(self, request):
        get_team_info = TeamMambarProfile.objects.all()
        context = {
            "team":get_team_info,
            "isact_team": "active"
        }
        return render(request, "team.html", context)


class Blog(View):

    def get(self, request):
        get_team_info = TeamMambarProfile.objects.all()
        context = {
            "team": get_team_info,
            "isact_team": "active"
        }
        return render(request, "blog-left-sidebar.html", context)



class StudyCase(View):

    def get(self, request):
        case_data= CaseStudy.objects.all()
        context = {
            "case_data":case_data,
            "isact_portfolio": "active"
        }
        return render(request, "case-study.html", context)


class StudyCaseDetails(View):

    def get(self, request):
        case_data= CaseStudy.objects.all()
        context = {


        }
        return render(request, "case_study_details.html", context)


class Result(View):

    def get(self, request):
        get_image = PortfolioImage.objects.all()
        context = {
            "get_image":get_image,
            "isact_portfolio": "active"
        }
        return render(request, "result.html", context)


class EmailWorks(View):

    def get(self, request):

        context = {

            "isact_portfolio": "active"
        }
        return render(request, "how_email_works.html", context)


def contact(request):
    obj = OfficialContactInformation.objects.last()

    context={
        "obj":obj,
    }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        message_obj = Contact(name=name, email=email,subject=subject,message=message)
        message_obj.save()
        messages.success(request, 'Profile details updated.')
        return redirect("contact")
    return render(request, "contact.html", context)


def TeamAugmentation(request):
    return render(request, "service/team_augomentation.html")


def FixedPriceProjects(request):
    return render(request, "service/fixed_price_projects.html")


def ProjectConsulting(request):
    return render(request, "service/project_consulting.html")


def SupportMaintenance(request):
    return render(request, "service/support_maintenance.html")


def CustomSoftwareDevelopment(request):
    return render(request, "experties/custom_software_Development.html")






def AzureAws(request):
    return render(request, "experties/azureAwz.html")


def DataScience(request):
    return render(request, "experties/datascience.html")


def DevOps(request):
    return render(request, "experties/devOps.html")


def MobileAppDevelopment(request):
    return render(request, "experties/mobile_app_development.html")


def SQATrainging(request):
    return render(request, "experties/qatraning.html")


def UiUxDesign(request):
    return render(request, "experties/ui_ux_design.html")


def WebApplicationDevelopment(request):
    return render(request, "experties/web_application_development.html")

