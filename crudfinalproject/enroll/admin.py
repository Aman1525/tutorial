from django.contrib import admin
from enroll.models import user

# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display=['id','name','email','password']

admin.site.register(user,useradmin)
