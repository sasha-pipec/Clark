from django.contrib import admin

from models_app.models import UserDirectMessage
from models_app.models.direct_message.models import DirectMessage


class UserDirectMessageInline(admin.TabularInline):
    model = UserDirectMessage


@admin.register(DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    inlines = (UserDirectMessageInline,)
