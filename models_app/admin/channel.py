from django.contrib import admin

from models_app.models import UserChannel
from models_app.models.channel.models import Channel


class UserChannelInline(admin.TabularInline):
    model = UserChannel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    inlines = (UserChannelInline,)
