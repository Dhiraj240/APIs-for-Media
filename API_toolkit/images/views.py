from django.shortcuts import render

from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import image
from . serializers import imageSerializer


class imagelist(APIView):

	def get(self, request):
		image1 = image.objects.all()
		serializer = imageSerializer(image1, many = True)
		return Response(serializer.data)
