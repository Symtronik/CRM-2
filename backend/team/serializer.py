from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Team


class UserSerlializer(serializers.ModelSerializer):
    class Meta:(
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )
    )

class TeamSerlializer(serializers.ModelSerializer):
    members = UserSerlializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "members",
        )
