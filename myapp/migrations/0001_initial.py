# Generated by Django 2.0.3 on 2024-03-12 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assign_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleno', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Busassign_driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BUS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Busassign_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BUS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.bus')),
            ],
        ),
        migrations.CreateModel(
            name='childassign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('licenseno', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('usertype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('DRIVER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Login')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Login')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('clas', models.CharField(max_length=50)),
                ('division', models.CharField(max_length=50)),
                ('STAFF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tips', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('EXPERT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Expert')),
            ],
        ),
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('STAFF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Staff')),
            ],
        ),
        migrations.AddField(
            model_name='expert',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Login'),
        ),
        migrations.AddField(
            model_name='driver',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Login'),
        ),
        migrations.AddField(
            model_name='childassign',
            name='PARENT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.parent'),
        ),
        migrations.AddField(
            model_name='childassign',
            name='STUDENT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Student'),
        ),
        migrations.AddField(
            model_name='busassign_student',
            name='STUDENT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Student'),
        ),
        migrations.AddField(
            model_name='busassign_driver',
            name='DRIVER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Driver'),
        ),
        migrations.AddField(
            model_name='attendence',
            name='STUDENT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Student'),
        ),
        migrations.AddField(
            model_name='assign_work',
            name='STUDENT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Student'),
        ),
        migrations.AddField(
            model_name='assign_work',
            name='WORK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.work'),
        ),
    ]
