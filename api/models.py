from django.db import models as nmodels
from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(nmodels.Model):
    user = nmodels.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)

    #Additional Information
    department = nmodels.CharField(max_length=20)
    phone_number = nmodels.CharField(max_length = 15, blank = True)
    profile_pic = nmodels.ImageField(upload_to="profile_pics", blank=True)
    created_at = nmodels.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email


class Route(models.Model):
    name = models.CharField(max_length=254)
    route_id = models.CharField(max_length=254)
    avg_depth = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)


class Bathy(models.Model):
    depth = models.FloatField()
    long = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPointField(srid=4326)


class Jetty(models.Model):
    name = models.CharField(max_length=254)
    terminal = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

class Depth(models.Model):
    value = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

class DepthA(models.Model):
    value = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

class DepthB(models.Model):
    value = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

class DepthC(models.Model):
    value = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)


class DepthD(models.Model):
    value = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

