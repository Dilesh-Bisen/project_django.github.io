# Generated by Django 5.0 on 2023-12-30 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegi', '0005_subject_subjectmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmarks',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vegi.subject'),
        ),
    ]