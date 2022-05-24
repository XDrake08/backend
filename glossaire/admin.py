# from django.contrib import admin
# from .models import Glossary
# # Register your models here.
# from import_export.admin import ImportExportModelAdmin

# @admin.register(Glossary)
# class ViewAdmin(ImportExportModelAdmin):
#   pass

from django.contrib import admin
from .models import Glossary
admin.site.register(Glossary)
