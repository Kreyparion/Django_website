from django.contrib import admin

# Register your models here.
from .models import Presta


class PrestaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['presta_name']}),
        ('Date information', {'fields': [
         'pub_date', 'presta_date'], 'classes': ['collapse']}),
    ]
    list_display = ('presta_name', 'presta_date', 'pub_date')
    list_filter = ['presta_date']
    search_fields = ['presta_name']


admin.site.register(Presta, PrestaAdmin)
