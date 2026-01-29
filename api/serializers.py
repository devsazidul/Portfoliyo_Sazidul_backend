from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Document, ContactMessage, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']

class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Project
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    fileUrl = serializers.CharField(source='file_url') # Frontend sends camelCase

    class Meta:
        model = Document
        fields = ['id', 'title', 'description', 'type', 'category', 'fileUrl', 'size']

class ContactMessageSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = ContactMessage
        fields = '__all__'
