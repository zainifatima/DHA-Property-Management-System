from django.contrib import admin
from website_app.models import Property
from website_app.models import Category_registration
from website_app.models import Contact_data

# Register your models here.
admin.site.register(Property)
admin.site.register(Category_registration)
admin.site.register(Contact_data)
# @admin.register(Property)
# class Propertyadmin(admin.ModelAdmin):
#     list_display = ('name','agency','phone','addre')
