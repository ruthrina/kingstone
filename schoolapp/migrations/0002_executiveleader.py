# Generated by Django 5.0.2 on 2025-01-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutiveLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='executives/')),
                ('quote', models.TextField()),
            ],
        ),
    ]
