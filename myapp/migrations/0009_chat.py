# Generated by Django 2.0.3 on 2024-03-14 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_locate'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('type', models.CharField(default=1, max_length=255)),
                ('EXPERT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Expert')),
                ('PARENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.parent')),
            ],
        ),
    ]
