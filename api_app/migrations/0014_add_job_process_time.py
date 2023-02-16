# Generated by Django 3.2.18 on 2023-02-16 11:02

from django.db import migrations, models


def calculate_process_time(apps, schema_editor):
    Job = apps.get_model("api_app", "Job")
    for job in Job.objects.all():
        if job.finished_analysis_time:
            job.process_time = job.calculate_process_time()
            job.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0013_alter_job_observable_classification"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="process_time",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.RunPython(calculate_process_time, migrations.RunPython.noop),
    ]
