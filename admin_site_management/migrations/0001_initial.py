# Generated by Django 4.0 on 2021-12-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(auto_now=True)),
                ('is_responded', models.BooleanField(default=False)),
                ('resolved_date', models.DateTimeField(blank=True, null=True)),
                ('is_removed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
