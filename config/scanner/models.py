from django.db import models
from events.models import Event

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'student_id')

    def __str__(self):
        return f"{self.student_id} at {self.event.name}"