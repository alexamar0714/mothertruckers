from rest_framework import serializers
from api.models import Position
import uuid

class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('user_id', 'new_long', 'new_lat', 'old_long', 'old_lat', 'prob_ctr', 'alert')

