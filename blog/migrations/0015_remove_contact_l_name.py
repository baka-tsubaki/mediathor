# Generated by Django 3.2 on 2021-04-15 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='l_name',
        ),
    ]