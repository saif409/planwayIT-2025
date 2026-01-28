from django.contrib import admin

# Register your models here.
from . models import Contact,OfficialContactInformation,TeamMambarProfile,Clients,PortfolioImage,CaseStudy

admin.site.register(Contact)
admin.site.register(OfficialContactInformation)
admin.site.register(TeamMambarProfile)
admin.site.register(Clients)
admin.site.register(PortfolioImage)
admin.site.register(CaseStudy)

