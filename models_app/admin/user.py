from django.contrib import admin

from models_app.models.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', )
