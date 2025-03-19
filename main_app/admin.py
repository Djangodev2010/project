from django.contrib import admin
from .models import Course, Founder, Review

# Register your models here.

admin.site.register(Course)
admin.site.register(Founder)
admin.site.register(Review)
