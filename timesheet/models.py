# timesheets/models.py
from django.db import models
from django.utils import timezone

class Timesheet(models.Model):
    STATUS_CHOICES = (("draft", "Draft"), ("submitted", "Submitted"))

    contractor = models.CharField(max_length=200)
    contract_no = models.CharField(max_length=200, blank=True)
    assigned_location = models.CharField(max_length=255, blank=True)
    project_title = models.CharField(max_length=500, blank=True)
    team = models.CharField(max_length=200, blank=True)
    month = models.IntegerField()
    year = models.IntegerField()
    prepared_by = models.CharField(max_length=200, blank=True)
    client_rep = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project_title} - {self.month}/{self.year} ({self.contractor})"


class TimesheetEntry(models.Model):
    timesheet = models.ForeignKey(Timesheet, related_name="entries", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    discipline = models.CharField(max_length=200, blank=True)
    # JSONField works in modern Django (>=3.1) and in all DBs:
    attendance = models.JSONField(default=dict, blank=True)
    total = models.IntegerField(default=0)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.timesheet_id})"
    
class Signer(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)  # unique signing code

    def __str__(self):
        return f"{self.name} ({self.role})"

    
    
class Signature(models.Model):
    timesheet = models.ForeignKey(
        Timesheet,
        related_name="signatures",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default="STIS")
    signed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.role} ({self.timesheet.id})"

