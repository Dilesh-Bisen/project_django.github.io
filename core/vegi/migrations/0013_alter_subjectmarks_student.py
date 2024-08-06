# Generated by Django 5.0 on 2024-01-02 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegi', '0012_student_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmarks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_marks', to='vegi.student'),
        ),
    ]