# Generated by Django 4.1.3 on 2023-01-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume_angajat', models.CharField(max_length=100)),
                ('profesie', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]