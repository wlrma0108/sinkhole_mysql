from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.incident_list, name='incident_list'),                  # 사고 리스트
    path('new/', views.incident_create, name='incident_create'),          # 사고 등록
    path('edit/<int:pk>/', views.incident_update, name='incident_update'),# 사고 수정
    path('delete/<int:pk>/', views.incident_delete, name='incident_delete'), # 사고 삭제
    path('stats/', views.stats_view, name='stats'),                       # 통계 보기
]
