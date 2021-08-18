from django.contrib import admin
from .models import Subject
from tinymce.widgets import TinyMCE
from django.db import models

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

    # replaces default TextField widget with TinyMCE editor
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Subject, SubjectAdmin) # adds Subject into admin console