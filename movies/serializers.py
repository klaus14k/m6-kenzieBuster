from rest_framework import serializers
from movies.models import Movie, MovieRatings

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default="")
    rating = serializers.ChoiceField(choices=MovieRatings.choices, default=MovieRatings.GENERAL)
    synopsis = serializers.CharField(allow_null=True, default="")
    added_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)