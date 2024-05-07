# Generated by Django 5.0.4 on 2024-04-30 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('birth_data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updataed_at', models.DateTimeField(auto_now=True, null=True)),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('organization', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updataed_at', models.DateTimeField(auto_now=True, null=True)),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('contract', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], default='new', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updataed_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentSponser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updataed_at', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.sponsor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.university'),
        ),
    ]
