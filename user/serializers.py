from django.db import models
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        # This means password only can be write able, while returning response
        # password field wont be return 
        extra_kwargs = {
            'password': { 'write_only': True},

            }
        

    def create(self, validated_data):
        # Here We Remove password field from validated_data dictionary and 
        # store it in vairable and passing None object
        password = validated_data.pop('password', None)
        # Pass validated_data dictionary to create model instance without password field
        instance = self.Meta.model(**validated_data)
        # Check for password field and save it in HASH format
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
