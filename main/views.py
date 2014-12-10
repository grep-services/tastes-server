from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Image, Location, Tag

# for rest
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from main.serializers import ImageSerializer
# from main.forms import ImageForm

# Create your views here.

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def image_add(request):
	if request.method == 'POST': # not for switch just block any other methods.
		# there are many ways to do it however first go through fast and simple way.
		image = Image.objects.create()
		image.origin = request.FILES['image']
		image.save()

		return HttpResponse('success')
		
	return HttpResponse('failed')

@csrf_exempt
def image_list(request):
	images = Image.objects.all()
	serializer = ImageSerializer(images, many=True)
	return JSONResponse(serializer.data)
