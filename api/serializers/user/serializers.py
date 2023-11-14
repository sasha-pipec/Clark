from rest_framework import serializers

from models_app.models import User, Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    users_count = serializers.SerializerMethodField()

    def get_users(self, obj):
        users = obj.users.all()
        if users.count() > 5:
            return UserImageSerializer(users[:5], many=True).data
        return UserImageSerializer(users, many=True).data

    def get_users_count(self, obj):
        return obj.users.all().count()

    class Meta:
        model = Workspace
        fields = (
            'id',
            'name',
            'image',
            'users',
            'users_count'
        )


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'image',
        )


class UserDetailSerializer(serializers.ModelSerializer):
    workspaces = serializers.SerializerMethodField()

    def get_workspaces(self, obj):
        return WorkspaceSerializer(obj.workspase_set.all(), many=True).data

    class Meta:
        model = User
        fields = (
            'email',
            'workspaces'
        )
