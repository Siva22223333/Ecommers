from rest_framework import serializers
from .models import Useraccount

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraccount
        fields = ['name', 'mobileno', 'email', 'password', 'address', 'token']
        
    def create(self, validated_data):
        return Useraccount.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class SignIngetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraccount
        fields = '__all__'
