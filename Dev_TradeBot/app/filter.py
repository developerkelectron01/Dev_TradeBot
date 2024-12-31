import django_filters
from .models import UserType

class MasterFilter(django_filters.FilterSet):
    user_type = django_filters.CharFilter(field_name='user_type')
    email = django_filters.CharFilter(field_name='email')
    class Meta:
        model = UserType
        fields = ['user_type', 'email']
