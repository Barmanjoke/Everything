from pyexpat import model
from django.db import models
from achievements import models
from achievements.models import *

from achievements import models as dbh

class Titles(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    class Meta:
        db_table = 'titles'

class title_holders(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    title = models.ForeignKey('Titles', models.DO_NOTHING)

    class Meta:
        db_table = 'title_holders'

class Badges(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    association = models.ForeignKey('Associations', models.DO_NOTHING)
    event = models.ForeignKey('Events', models.DO_NOTHING)
    imageurl = models.URLField()

    description = models.CharField(max_length=300)

    class Meta:
        db_table = 'badges'

class badge_holders(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    badge = models.ForeignKey('Badges', models.DO_NOTHING)

    class Meta:
        db_table = 'badge_holders'
