from  rest_framework import serializers
from  .models import Master

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields =    '__all__'

# class ChildSerializer(serializers.ModelSerializer):
#     master = MasterSerializer()
#     class Meta:
#         model = Master
#         fields = ['id', 'child_name', 'master']