from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', views.incident_list, name='incident_list'),
    path('new/', views.incident_create, name='incident_create'),
    path('<int:pk>/', views.incident_detail, name='incident_detail'),
    path('incidents/', include('sinkhole.urls')),
    path('admin/', admin.site.urls),
    path('incidents/', include('incidents.urls')),
]
