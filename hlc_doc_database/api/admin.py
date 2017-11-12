from django.contrib import admin

# Register your models here.

from .models import DocMetadata

class AdminDoc(admin.ModelAdmin):
    readonly_fields = ('upload_date',)

admin.site.register(DocMetadata, AdminDoc)