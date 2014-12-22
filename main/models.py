# from django.db import models
from django.contrib.gis.db import models

# Create your models here.

"""
char field : max 256 but should define it. not null default
one to one : cascade deletes by default
many to many : not cascade on deletes
"""
# doesn't seems nginx uses link of media, static so set it directly until the solution found
# now uses media and media root of settings.
class Image(models.Model):
	origin = models.ImageField(upload_to='origin')
	thumbnail = models.ImageField(upload_to='thumbnail')
	date = models.DateTimeField(auto_now_add=True)
	
	# location = models.OneToOneField('Location', null=True, on_delete=models.SET_NULL)
        address = models.CharField(max_length=200, null=True) # it is possible that only coordinates exists except for address
	# can be true with address.
        point = models.PointField(srid=4326, null=True) # later, translation of point by json will be done. not now. - can be done by rest-gis lib.
	# instant distance. positive natural number.
	# dist = models.PositiveIntegerField(null=True)
	dist = models.CharField(max_length=25, null=True) # splitting takes more time. just send str and let client do that process.

	tag = models.ManyToManyField('Tag', null=True) # there exists problem that 0-taged image
	# for using distance(), order_by()
	objects = models.GeoManager()
	
	# save. for thumbnail.
	
	def create_thumbnail(self):
                if not self.origin:
                        return

                if self.thumbnail:
                        return
		
		from PIL import Image
		from cStringIO import StringIO
		from django.core.files.base import ContentFile

		image = Image.open(self.origin)
		resized = image.resize((320, 320), Image.ANTIALIAS) # galaxy 5 1080, iphone 5 640 so 320 enough
		handler = StringIO()

		try:
			resized.save(handler, image.format) # save resized to handler with format of the 'image'
			self.thumbnail.save(self.origin.name, ContentFile(handler.getvalue()))
		finally:
			handler.close()
		
	def save(self, *args, **kwargs):
		self.create_thumbnail()

		super(Image, self).save(*args, **kwargs)
	
	# delete files on object deletion. db rows will be also deleted cause of cascade option.
	def delete(self, *args, **kwargs):
		self.origin.delete()
		self.thumbnale.delete()
		super(Image, self).delete(*args, **kwargs)
# at now, attatch to image. later. seperate it from image and integrate it. that will be useful.
"""
class Location(models.Model):
	address = models.CharField(max_length=200, null=True) # it is possible that only coordinates exists except for address
	point = models.PointField(srid=4326) # later, translation of point by json will be done. not now.
"""
class Tag(models.Model):
	name = models.CharField(max_length=50)
