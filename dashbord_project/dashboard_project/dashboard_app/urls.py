from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/<int:plan_id>/', views.dashboard, name='dashboard'),
    path('api/save/', views.save_dashboard, name='save_dashboard'),
    path('api/load/<str:month>/', views.load_dashboard, name='load_dashboard'),
    path('api/export/<int:plan_id>/', views.export_excel, name='export_excel'),
]