from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TimesheetViewSet, validate_signature_code

router = DefaultRouter()
router.register(r"timesheets", TimesheetViewSet, basename="timesheet")

urlpatterns = [
    path("", include(router.urls)),  # ✅ includes /timesheets/ routes
    path("validate-signature/", validate_signature_code, name="validate-signature"),  # ✅ keeps validation route
]
