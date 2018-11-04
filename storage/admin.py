from django.contrib import admin
from .models import FileModel


admin.register(FileModel)(admin.ModelAdmin)

