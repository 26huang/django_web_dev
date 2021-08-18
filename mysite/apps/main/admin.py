from django.contrib import admin
from .models import Subject


# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    """
    Allows ordering of fields in admin display.
    Use either fields or fieldsets but not both.
    """
    # fields = ['title',
    #           'published',
    #           'content']
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Summary', {'fields': ['published', 'content']})
    ]

admin.site.register(Subject, SubjectAdmin) # adds Subject into admin console