from django.contrib import admin

# Register your models here.
from .models import Profile,Book
admin.site.register(Profile)
admin.site.register(Book)

