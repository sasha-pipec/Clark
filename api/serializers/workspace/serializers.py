from rest_framework import serializers

from api.serializers.user.serializers import UserImageSerializer
from models_app.models import Workspace


# class WorkspaceSerializer(serializers.ModelSerializer):
#     users = serializers.SerializerMethodField()
#     users_count = serializers.SerializerMethodField()
#
#     def get_users(self, obj):
#         users = obj.users.all()
#         if users.count() > 5:
#             return UserImageSerializer(users[:5], many=True).data
#         return UserImageSerializer(users, many=True).data
#
#     def get_users_count(self, obj):
#         return obj.users.all().count()
#
#     class Meta:
#         model = Workspace
#         fields = (
#             'name',
#             'image',
#             'users',
#             'users_count'
#         )
