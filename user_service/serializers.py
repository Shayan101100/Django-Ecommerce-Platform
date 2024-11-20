
from django.utils.timezone import now
from .models import UserInfo
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id',
                  'username',
                  'fullname',
                 'email',
                'phon_number',
               'address',
              'city',
             'country',
            'postal_code',
           'policy_agreement',
          'agreement_timestamp',
          ]
    def validate(self, data):
        required_fields = [
                  'username',
                  'fullname',
                 'email',
                'phon_number',
               'address',
              'city',
             'country',
            'postal_code',
           'policy_agreement',
          ]
        for field in required_fields:
            if not data.get(field):
                raise ValidationError(f"The {field} field connot be empty")
        if data.get("policy_agreement"):
            data["agreement_timestamp"] = now
        else:
            data["agreement_timestamp"] = None
        return data
    
    def validate_password(self, value):
        """validates the password field"""
        validate_password(value)
        return value
    
    def create(self, validated_data):
        if validated_data.get("policy_agreement"):
            validated_data["agreement_timestamp"] = now()
        user = UserInfo.objects.create_user(**validated_data)
        return user
    
        