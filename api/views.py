from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, jettySerializer, routeSerializer, bathySerializer, UserInfoSerializer, depthSerializer, depthASerializer, depthBSerializer, depthCSerializer, depthDSerializer
from .models import Route, Bathy, Jetty, UserProfileInfo, Depth, DepthA, DepthB, DepthC, DepthD


# Create your viewsets here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset= UserProfileInfo.objects.all()
    serializer_class = UserInfoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class bathyViewSet(viewsets.ModelViewSet):
    queryset = Bathy.objects.all()
    serializer_class = bathySerializer


class routeViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = routeSerializer


class jettyViewSet(viewsets.ModelViewSet):
    queryset = Jetty.objects.all()
    serializer_class = jettySerializer

class depthViewSet(viewsets.ModelViewSet):
    queryset = Depth.objects.all()
    serializer_class = depthSerializer

class depthAViewSet(viewsets.ModelViewSet):
    queryset = DepthA.objects.all()
    serializer_class = depthASerializer

class depthBViewSet(viewsets.ModelViewSet):
    queryset = DepthB.objects.all()
    serializer_class = depthBSerializer

class depthCViewSet(viewsets.ModelViewSet):
    queryset = DepthC.objects.all()
    serializer_class = depthCSerializer

class depthDViewSet(viewsets.ModelViewSet):
    queryset = DepthD.objects.all()
    serializer_class = depthDSerializer

