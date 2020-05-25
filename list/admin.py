from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Agra,Aligarh,Auraiya,Etah,Etawah,Farrukhabad,Firozabad,Hathras,Kasganj,Kannauj,Mathura,Mainpuri,Aligarh_c)
class ViewAdmin(ImportExportModelAdmin):
    pass
