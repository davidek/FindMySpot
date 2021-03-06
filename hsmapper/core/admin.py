"""
Admin module for hsmapper core app
"""

from django.contrib import admin
import reversion
from core.models import Pathology, MedicalService, FacilityType, Facility, \
                    OpeningTime, SpecialDay


class ReversionAdmin(reversion.VersionAdmin):
    """ Wrapper class for django-reversion """
    pass


admin.site.register(Pathology)
admin.site.register(MedicalService)
admin.site.register(FacilityType)
admin.site.register(Facility, ReversionAdmin)
admin.site.register(OpeningTime)
admin.site.register(SpecialDay)
