from django.contrib.gis import admin
from .models import Route, Jetty, Bathy, UserProfileInfo, Depth, DepthA, DepthB, DepthC, DepthD
#from leaflet.admin import LeafletGeoAdmin

# Register your models here.
admin.site.register(Route)
admin.site.register(Bathy)
admin.site.register(Jetty)
admin.site.register(UserProfileInfo)
admin.site.register(Depth)
admin.site.register(DepthA)
admin.site.register(DepthB)
admin.site.register(DepthC)
admin.site.register(DepthD)