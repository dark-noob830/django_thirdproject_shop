# Generated by Django 5.1.3 on 2024-11-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('code', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
