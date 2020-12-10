from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ServiceSerializer
from .models import Service


@api_view(['GET'])
def services_info(request):
    posts = Service.objects.all()
    serializer = ServiceSerializer(posts, many=True)
    return Response(serializer.data)

