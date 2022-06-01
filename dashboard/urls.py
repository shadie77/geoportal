from os import name
from django.urls import path
from dashboard.views import logon, DashboardView, index, user_logout, KeplerDashboardView, SlideoutView, AppearView
from django.contrib.auth.decorators import login_required, permission_required


# Create the views here
urlpatterns = [
    path("", index.as_view(), name='homepage'),
    path('login/', logon.as_view(), name= 'login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('signout/', user_logout, name = "signout"),
    path('kepler/', KeplerDashboardView.as_view(), name = "kepler"),
    path('slidout/', SlideoutView.as_view(), name='slideout'),
    path('appear/',AppearView.as_view(), name= "appear")
]