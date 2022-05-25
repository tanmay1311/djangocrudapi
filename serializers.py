from django.db.models import fields
from rest_framework import serializers
from .models import Item
  
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'username', 'age', 'dob')
        extra_kwargs = { 'name': {'required': False},'username': {'required': False},'age': {'required': False},'dob': {'required': False}}