from django.shortcuts import render, redirect
from scanner.models import Attendance
from .models import Event
from .forms import EventForm  # We'll create this next

def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/event_list.html', {'events': events})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_create.html', {'form': form})

def dashboard(request):
    recent_events = Event.objects.order_by('-date')[:5]
    recent_attendance = Attendance.objects.select_related('event').order_by('-timestamp')[:10]
    return render(request, 'dashboard/dashboard.html', {
        'recent_events': recent_events,
        'recent_attendance': recent_attendance
    })