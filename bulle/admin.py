from django.contrib import admin
from .models import Recipies
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipies)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')

