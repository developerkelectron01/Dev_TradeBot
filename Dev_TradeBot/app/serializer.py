from  rest_framework import serializers
from  .models import UserType

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'
        # exclude = ['created', 'updated']
        extra_kwargs = {
            'master_id': {'read_only': True}
        }
