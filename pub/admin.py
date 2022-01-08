from django.contrib import admin
from .models import BookedModel, TableModel

# Register your models here.

admin.site.register(BookedModel)
admin.site.register(TableModel)
