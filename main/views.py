from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Image

# for rest
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from main.serializers import UserSerializer, GroupSerializer
from main.serializers import ImageSerializer

# Create your views here.

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def get_image(request):
	image = Image.objects.get(pk=3)

	text = image.origin.url
	text += '<p><img src="{image_url}"/></p>'

	return HttpResponse(text.format(
		image_url = image.origin.url
		)
	)

@csrf_exempt
def image_list(request):
	images = Image.objects.all()
	serializer = ImageSerializer(images, many=True)
	return JSONResponse(serializer.data)
"""
class UserViewSet(viewsets.ModelViewSet):
    
    # API endpoint that allows users to be viewed or edited.
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    
    # API endpoint that allows groups to be viewed or edited.
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
"""
