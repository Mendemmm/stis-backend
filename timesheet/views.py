from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Timesheet, Signer
from .serializers import TimesheetSerializer, SignatureUserSerializer


class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = Timesheet.objects.all().order_by("-id")
    serializer_class = TimesheetSerializer
    permission_classes = [AllowAny]  # adjust as needed


@api_view(["POST"])
def validate_signature_code(request):
    """
    Dynamically validate a signer code from the database.
    """
    code = request.data.get("code")
    print("DEBUG received code:", code)
    if not code:
        return Response(
            {"valid": False, "error": "No code provided"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        signer = Signer.objects.get(code=code)
        user = {
            "name": signer.name,
            "role": signer.role,
            "department": signer.department,
        }
        serializer = SignatureUserSerializer(user)
        return Response({"valid": True, "user": serializer.data}, status=status.HTTP_200_OK)

    except Signer.DoesNotExist:
        return Response(
            {"valid": False, "error": "Invalid code"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
