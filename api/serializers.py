from rest_framework import serializers
from .models import student

class ShowStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['id', 'name']

class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['name', 'age', 'city']