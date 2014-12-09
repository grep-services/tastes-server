from django.db import models

# Create your models here.

"""
char field : max 256 but should define it. not null default
foreign key : cascade deletes by default
"""
"""
class Item(models.Model):
	image = models.ForeignKey('Image')
	location = models.ForeignKey('Location')
	tag = models.ForeignKey('Tag')
"""
# doesn't seems nginx uses link of media, static so set it directly until the solution found
# now uses media and media root of settings.
class Image(models.Model):
	origin = models.ImageField(upload_to='origin')
	thumbnail = models.ImageField(upload_to='thumbnail')
	date = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=200)
	latitude = models.FloatField()
	longitude = models.FloatField()

	# delete files on object deletion. db rows will be also deleted cause of cascade option.
	def delete(self, *args, **kwargs):
		self.origin.delete()
		self.thumbnale.delete()
		super(Image, self).delete(*args, **kwargs)
"""
class Location(models.Model):
	address = models.CharField(max_length=200)
	latitude = models.FloatField()
	longitude = models.FloatField()
"""
class Tag(models.Model):
	name = models.CharField(max_length=50)
	image = models.ForeignKey(Image)
