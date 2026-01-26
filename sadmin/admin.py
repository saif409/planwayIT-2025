from django.contrib import admin

# Register your models here.
from . models import Contact,OfficialContactInformation,TeamMambarProfile,Clients,PortfolioImage

admin.site.register(Contact)
admin.site.register(OfficialContactInformation)
admin.site.register(TeamMambarProfile)
admin.site.register(Clients)
admin.site.register(PortfolioImage)

