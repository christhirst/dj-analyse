from django.contrib import admin
from .models import Data




class PostModelAdmin(admin.ModelAdmin):
    list_display = ["table_name", "uploader", "created", "updated"]
    class Meta:
        model = Data

admin.site.register(Data, PostModelAdmin)