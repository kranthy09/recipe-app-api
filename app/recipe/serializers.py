"""
Serializers for recipe APIs
"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.Serializer):
    """Serialzer for recipes."""

    class Meta:
        model = Recipe
        fields = ["id", "title", "time_minutes", "price", "link"]
        read_only_fields = [
            "id",
        ]


class RecipeDetailSerialzer(serializers.ModelSerializer):
    """Serializer for recipe detail view"""

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "time_minutes",
            "price",
            "link",
            "description",
        ]
