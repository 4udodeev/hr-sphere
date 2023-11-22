from django.contrib import admin

from .models import *

admin.site.register(ContractType)
admin.site.register(ContractFile)
admin.site.register(Contract)
admin.site.register(Region)
admin.site.register(Place)
admin.site.register(EventFile)
admin.site.register(Event)
admin.site.register(TypeOfCertificate)
admin.site.register(CertificateFile)
admin.site.register(Certificate)
admin.site.register(PollEntry)
admin.site.register(PollQuestion)
admin.site.register(Poll)
admin.site.register(PollResult)