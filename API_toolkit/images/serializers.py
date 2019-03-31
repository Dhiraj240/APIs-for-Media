from rest_framework import serializers
from images.models import image

class imageSerializer(serializers.ModelSerializer):

	class Meta:
		model = image
		# reterieve every field
		fields = '__all__'