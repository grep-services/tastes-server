from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Image, Tag

# for rest
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from main.serializers import ImageSerializer, TagSerializer

# for gis
from django.contrib.gis.geos import *
from django.contrib.gis.measure import Distance, D

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
		if address != None: # seperated from coordinate now.
			image.address = address

		latitude = request.POST.get('latitude', None)
		longitude = request.POST.get('longitude', None)

		if latitude != None and longitude != None: # address can be null
			image.point = Point(float(latitude), float(longitude))
			# image.point = Point(1.234, 1.234)
			# image.location = Location.objects.create(address = address, point = point)

		tag_str = request.POST.get('tag', None) # actually not null by client. and doesn't need format checking also.
		if tag_str != None:
			# google plugin tester sends chars strangely, so tested by phone directly.
			tag_list = map(lambda str : str.strip(), tag_str.split(',')) # space parsing as a base.(for viewing)
			for tag in tag_list:
				# case insensitive later
				image.tag.add(Tag.objects.get_or_create(name = tag)[0]) # duplication cannot happen.
			
		image.save() # at least 1 tag remains even though other location, tags are not exists.

		return HttpResponse('success')
		
	return HttpResponse('failed')

@csrf_exempt
def image_tag(request): # add tag to image with image id. actually editing image.
	if request.method == 'POST':
		image_id = request.POST.get('id', None)

		if image_id != None:
			try:
				image = Image.objects.get(pk = image_id)

				tag_name = request.POST.get('tag', None)
				if tag_name != None:
					# it seems that django automatically cares about duplcation of many-to-many items. now don't care.
					image.tag.add(Tag.objects.get_or_create(name = tag_name)[0]) # case insensitive later
					image.save()

					return HttpResponse('success to save tag')
			except:
				return HttpResponse('failed. no image matching to the id')

		return HttpResponse('failed. no id')

	return HttpResponse('failed')

@csrf_exempt
def image_get(request): # get one image
	if request.method == 'POST':
		image_id = request.POST.get('id', None)

		if image_id != None:
			image = Image.objects.get(pk = image_id)
			serializer = ImageSerializer(image)
			return JSONResponse(serializer.data)

	return HttpResponse('failed')

@csrf_exempt
def image_list(request):
	if request.method == 'POST':
		tag_str = request.POST.get('tag', None)
		if tag_str != None:
                        tag_list = map(lambda str : str.strip(), tag_str.split(','))
			tags = Tag.objects.filter(name__in = tag_list) # pick tags that name of which is in the list. case insensitive later also
			images = Image.objects.filter(tag__in = tags).distinct() # pick images that tag obj is in the given tag-list. - remove duplicates using distinct()

			latitude = request.POST.get('latitude', None)
			longitude = request.POST.get('longitude', None)
			if latitude != None and longitude != None:
	                        base = Point(float(latitude), float(longitude))
				# base.srid = 4326 => it is said that setting default srid is need before calling transform().
				limit = 3000 # maybe in meters
				near = images.filter(point__distance_lte = (base, D(m = limit))).distance(base).order_by('distance')
				# it can increase processing speed but not works yet.
				"""
				base.transform(900913)
				poly = base.buffer(distance * 0.000621 * 2172.344)
				near = images.filter(point__within = poly)
				"""
				# set dist by distance value.(couldn't find better way yet.)
				for image in near:
					image.dist = str(image.distance)
					image.save()

				serializer = ImageSerializer(near, many = True)
				return JSONResponse(serializer.data)
				# return HttpResponse(near[0].address)

	return HttpResponse('failed')

@csrf_exempt
def test(request):
	if request.method == 'POST':
		pnt = GEOSGeometry('SRID=4326;POINT(40.396764 -3.68042)')
		pnt2 = GEOSGeometry('SRID=4326;POINT(48.835797 2.329102)')
		d = pnt.distance(pnt2) * 100
		return HttpResponse(str(d))
	return HttpResponse('failed')

@csrf_exempt
def tag_list(request):
	if request.method == 'POST':
		tag_str = request.POST.get('tag', None)
		if tag_str != None:
			tags = Tag.objects.filter(name__contains = tag_str) # case insensitive later
			serializer = TagSerializer(tags, many = True)
			return JSONResponse(serializer.data)

	return HttpResponse('failed')
