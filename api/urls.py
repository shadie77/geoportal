from django.urls import path
from django.urls import path, include
from .views import UserViewSet, depthDViewSet, jettyViewSet, routeViewSet, bathyViewSet, depthViewSet, depthAViewSet, depthBViewSet, depthCViewSet, depthDSerializer
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('route', routeViewSet)
router.register('jetty', jettyViewSet)
router.register('bathy', bathyViewSet)
router.register('depth', depthViewSet)
router.register("deptha", depthAViewSet)
router.register('depthb', depthBViewSet)
router.register("depthc", depthCViewSet)
router.register("depthd", depthDViewSet)


urlpatterns = router.urls