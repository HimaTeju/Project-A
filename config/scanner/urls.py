from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.scanner_view, name='scanner'),
    path('<int:event_id>/process/', views.process_scan, name='process_scan'),  # Add this new view
    path('attendance/<int:event_id>/', views.attendance_list, name='attendance_list'),
]