from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'sec_name', 'last_name', 'date_of_birth', 'email', 'photo')
    list_display = ('first_name', 'sec_name', 'last_name', 'date_of_birth', 'email', 'photo')


admin.site.register(User, UserAdmin)
