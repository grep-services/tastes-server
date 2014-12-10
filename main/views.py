from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Image, Location, Tag

# for rest
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from main.serializers import ImageSerializer

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
		image = Image() # create method does save also.
		image.origin = request.FILES['image']
		image.save() # for many to many, image should have id.

		address = request.POST.get('address', None)
		latitude = request.POST.get('latitude', None)
		longitude = request.POST.get('longitude', None)

		if latitude != None and longitude != None: # address can be null
			image.location = Location.objects.create(address = address, latitude = latitude, longitude = longitude)

		tag_str = request.POST.get('tag', None) # actually not null by client. and doesn't need format checking also.
		if tag_str != None:
			# google plugin tester sends chars strangely, so tested by phone directly.
			tag_list = map(lambda str : str.strip(), tag_str.split(',')) # space parsing as a base.(for viewing)
			for tag in tag_list:
				image.tag.add(Tag.objects.get_or_create(name = tag)[0]) # duplication cannot happen.
			
		image.save() # at least 1 tag remains even though other location, tags are not exists.

		return HttpResponse('success')
		
	return HttpResponse('failed')

@csrf_exempt
def image_list(request):
	images = Image.objects.all()
	serializer = ImageSerializer(images, many=True)
	return JSONResponse(serializer.data)
