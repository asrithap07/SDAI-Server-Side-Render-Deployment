from rest_framework import serializers
from detection.models import UploadAlert

class UploadAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadAlert
        #took out 'pk'
        fields = ('id', 'image', 'user_ID', 'location', 'date_created', 'alert_receiver')

    def create(self, validated_data):
        return UploadAlert.objects.create(**validated_data)