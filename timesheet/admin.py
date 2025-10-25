# timesheet/admin.py
from django.contrib import admin
from .models import Timesheet, TimesheetEntry, Signature
from .models import Signer

class PersonnelEntryInline(admin.TabularInline):
    model = TimesheetEntry
    extra = 1
    fields = ('name', 'discipline', 'attendance', 'total', 'remarks')

class SignatureInline(admin.TabularInline):
    model = Signature
    extra = 0
    readonly_fields = ('name', 'role', 'department', 'company', 'signed_at')

@admin.register(Signer)
class SignerAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "department", "code")
    search_fields = ("name", "role", "department", "code")

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'contractor', 'assigned_location', 'month', 'year', 'status', 'prepared_by')
    inlines = [PersonnelEntryInline]

@admin.register(TimesheetEntry)
class PersonnelEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'timesheet', 'discipline', 'total')
    readonly_fields = ()

@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'department', 'company', 'signed_at', 'timesheet')
    list_filter = ('company', 'department', 'signed_at')
    search_fields = ('name', 'role', 'department')

