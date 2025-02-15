from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


# ----- Generic Relationships -----
'''
to define a generic relationship we need to define 3 fields
content_type
object_id
content_object
'''


class Tag (models.Model):
    label = models.CharField(max_length=255)


class TaggedItem (models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # type (product, video, article)
    # id
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # read the actual object that particiular tag applied to
    content_object = GenericForeignKey()


'''
LikedItem
    what user likes what object
    user : ForienKey to User
'''


class LikedItem (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
