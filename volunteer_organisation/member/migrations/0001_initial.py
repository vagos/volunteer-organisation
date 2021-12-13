# Generated by Django 3.2.9 on 2021-12-13 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('city_of_residense', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=13, null=True)),
            ],
        ),
    ]