# Generated by Django 2.0.3 on 2024-03-13 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_performance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='status',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
