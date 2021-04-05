from django.contrib import admin

# Register your models here.
from .models import Presta


class PrestaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['presta_name']}),
        ('Published', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
        ('Event information', {'fields': [
         'presta_type', 'presta_date', 'presta_end', 'presta_respo', 'presta_respo_mail']}),
    ]
    list_display = ('presta_name', 'presta_date',
                    'presta_type', 'presta_respo', 'pub_date')
    list_filter = ['presta_date']
    search_fields = ['presta_name']


admin.site.register(Presta, PrestaAdmin)
