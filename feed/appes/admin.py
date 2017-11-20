from django.contrib import admin
# from .models import Myfeed, Category
from .models import Myfeed


# admin.site.register(Category)

class MyfeedAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Myfeed, MyfeedAdmin)