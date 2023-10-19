from rest_framework import serializers
from .models import CEO

class CEOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CEO
        fields = ['name', 'first_year_active']