# Generated by Django 3.1.13 on 2021-08-18 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import nautobot.core.celery
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("extras", "0014_auto_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScheduledJobs",
            fields=[
                ("ident", models.SmallIntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ("last_update", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="ScheduledJob",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("task", models.CharField(max_length=200)),
                ("job_class", models.CharField(max_length=255)),
                ("interval", models.CharField(max_length=255)),
                (
                    "args",
                    models.JSONField(blank=True, default=list, encoder=nautobot.core.celery.NautobotKombuJSONEncoder),
                ),
                (
                    "kwargs",
                    models.JSONField(blank=True, default=dict, encoder=nautobot.core.celery.NautobotKombuJSONEncoder),
                ),
                ("queue", models.CharField(blank=True, default=None, max_length=200, null=True)),
                ("one_off", models.BooleanField(default=False)),
                ("start_time", models.DateTimeField()),
                ("enabled", models.BooleanField(default=True)),
                ("last_run_at", models.DateTimeField(blank=True, editable=False, null=True)),
                ("total_run_count", models.PositiveIntegerField(default=0, editable=False)),
                ("date_changed", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(blank=True)),
                ("approval_required", models.BooleanField(default=False)),
                ("approved_at", models.DateTimeField(blank=True, editable=False, null=True)),
                (
                    "approved_by_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="jobresult",
            name="schedule",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="extras.scheduledjob"
            ),
        ),
    ]
