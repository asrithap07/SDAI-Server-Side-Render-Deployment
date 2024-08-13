import django_filters
from django_filters import DateFilter, CharFilter

from .models import *
from .models import UploadAlert

class DetectionFilter(django_filters.FilterSet):

    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date=DateFilter(field_name="date_created", lookup_expr='lte')

    location = CharFilter(field_name='location', lookup_expr='icontains')
    alert_receiver = CharFilter(field_name='alert_receiver', lookup_expr='iContains')

    class Meta:
        model = UploadAlert
        fields = '__all__'
        exclude = ['customer', 'user_ID', 'image', 'uuid']

        '''
        filter_overrides = {
            models.ImageField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
        '''