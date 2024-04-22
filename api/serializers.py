from rest_framework import serializers
from .models import Newsletter, Contact, Voluteer

class NewletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id','email']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','name','email','message']

class VoluteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluteer
        fields = ['id','name','address','phone']
