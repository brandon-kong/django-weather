from django.contrib import admin
from weather.models import User, SavedLocation

# Register your models here.
admin.site.register(User)
admin.site.register(SavedLocation)