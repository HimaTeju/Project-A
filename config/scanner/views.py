from django.shortcuts import render, get_object_or_404
from events.models import Event
from .models import Attendance
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def scanner_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    attendees = Attendance.objects.filter(event=event).order_by('-timestamp')
    return render(request, 'scanner/scanner.html', {'event': event, 'attendees': attendees})

def attendance_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    attendees = Attendance.objects.filter(event=event).order_by('-timestamp')
    return render(request, 'scanner/attendance_list.html', {'event': event, 'attendees': attendees})

@csrf_exempt
def process_scan(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id)
        
        # Handle both JSON (scanner) and form-data (manual) submissions
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            student_id = data.get('student_id')
        else:
            student_id = request.POST.get('student_id')
        
        # Check for duplicates
        if Attendance.objects.filter(event=event, student_id=student_id).exists():
            return JsonResponse({'success': False, 'message': 'Already scanned'})
        
        # Record attendance
        Attendance.objects.create(event=event, student_id=student_id)
        return JsonResponse({'success': True, 'message': f'{student_id} recorded'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})