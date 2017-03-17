from django.contrib import admin
from donations.models import Campaign
from donations.models import Company
from donations.models import Contact
from donations.models import Envelope
from donations.models import Pledge

admin.site.register(Campaign)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Pledge)
admin.site.register(Envelope)
