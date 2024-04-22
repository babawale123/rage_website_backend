from django.shortcuts import render
from .serializers import NewletterSerializer,ContactSerializer,VoluteerSerializer
from .models import Newsletter, Contact, Voluteer

from rest_framework.response import Response
from rest_framework.views import APIView


class NewsletterView(APIView):
    def post(self,request):
        data = NewletterSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)

class ContactView(APIView):
    def post(self,request):
        data = ContactSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)
    
class VoluteerView(APIView):
    def post(self,request):
        data = VoluteerSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)
