from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import UserProfileInfo
from rest_framework.authtoken.models import Token
from .models import Route, Jetty, Bathy, Depth, DepthA, DepthB, DepthC, DepthD
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.auth.models import User


class UserInfoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UserProfileInfo
        fields= ['department', 'phone_number', 'profile_pic', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    profile = UserInfoSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile']
        depth= 2

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class jettySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Jetty
        geo_field = "geom"
        fields = "__all__"


class bathySerializer(GeoFeatureModelSerializer):
    class Meta:
        model= Bathy
        geo_field = "geom"
        fields= "__all__"

class routeSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Route
		geo_field = "geom"
		fields = "__all__"

class depthSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Depth
        geo_field = "geom"
        fields = "__all__"

class depthASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DepthA
        geo_field = "geom"
        fields = "__all__"

class depthBSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DepthB
        geo_field = "geom"
        fields = "__all__"

class depthCSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DepthC
        geo_field = "geom"
        fields = "__all__"

class depthDSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DepthD
        geo_field = "geom"
        fields = "__all__"