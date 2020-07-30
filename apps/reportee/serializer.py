from rest_framework import serializers
from django.contrib.auth import get_user_model as user_model
User = user_model()
from .models import ReporteeProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name','email','is_supervisor','is_manager','is_reportee',)


class ReporteeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ReporteeProfile
        fields = '__all__'
        
    