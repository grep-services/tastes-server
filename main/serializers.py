# -*- coding: utf-8 -*-

# from django.contrib.auth.models import User, Group
from rest_framework import serializers

# from main.models import Image, Location, Tag
from main.models import Image, Tag

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
"""
class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		# fields = ('id', 'origin', 'thumbnail', 'date', 'address', 'dist', 'tag', 'positions')
		fields = ('id', 'origin', 'thumbnail', 'time', 'point', 'dist', 'tag', 'tag_str', 'positions', 'orientations', 'passcode')
		depth = 1 # in docs, it deals with nested structure.

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('name',) # untill now, id doesn't need. important that it is tuple. comma needs.
