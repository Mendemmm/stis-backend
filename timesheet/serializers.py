from rest_framework import serializers
from .models import Timesheet, TimesheetEntry, Signature


# --- Signature serializer --- #
class SignatureSerializer(serializers.ModelSerializer):
    signed_at = serializers.DateTimeField(
        required=False,
        allow_null=True,
        input_formats=[
            "%Y-%m-%dT%H:%M:%S.%fZ",  # ISO format
            "%Y-%m-%dT%H:%M:%SZ",
            "%d/%m/%Y %H:%M:%S",
            "%d/%m/%Y, %H:%M:%S %p",
            "%d/%m/%Y, %I:%M:%S %p",
        ],
    )

    class Meta:
        model = Signature
        exclude = ("timesheet",)  # ✅ don't require FK from frontend


class SignatureUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    role = serializers.CharField()
    department = serializers.CharField()


# --- Entry serializer --- #
class TimesheetEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimesheetEntry
        fields = ("id", "name", "discipline", "attendance", "total", "remarks")
        read_only_fields = ("id",)


# --- Main timesheet serializer --- #
class TimesheetSerializer(serializers.ModelSerializer):
    entries = TimesheetEntrySerializer(many=True)
    signatures = SignatureSerializer(many=True, required=False)  # ✅ include signatures

    class Meta:
        model = Timesheet
        fields = (
            "id",
            "contractor",
            "contract_no",
            "assigned_location",
            "project_title",
            "team",
            "month",
            "year",
            "prepared_by",
            "client_rep",
            "status",
            "created_at",
            "updated_at",
            "entries",
            "signatures",
        )
        read_only_fields = ("id", "created_at", "updated_at")

    def create(self, validated_data):
        entries_data = validated_data.pop("entries", [])
        signatures_data = validated_data.pop("signatures", [])

        timesheet = Timesheet.objects.create(**validated_data)

        # create related entries
        for entry in entries_data:
            TimesheetEntry.objects.create(timesheet=timesheet, **entry)

        # create related signatures
        for sig in signatures_data:
            Signature.objects.create(timesheet=timesheet, **sig)

        return timesheet

    def update(self, instance, validated_data):
        entries_data = validated_data.pop("entries", None)
        signatures_data = validated_data.pop("signatures", None)

        # update main fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # update entries
        if entries_data is not None:
            instance.entries.all().delete()
            for entry in entries_data:
                TimesheetEntry.objects.create(timesheet=instance, **entry)

        # update signatures
        if signatures_data is not None:
            instance.signatures.all().delete()
            for sig in signatures_data:
                Signature.objects.create(timesheet=instance, **sig)

        return instance
