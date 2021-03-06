# Generated by Django 3.2 on 2021-04-16 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_remove_contact_l_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_category_choices', models.CharField(choices=[('AC', 'Actualité'), ('LT', 'Littérature'), ('CL', 'Culture'), ('EV', 'Evènement'), ('BS', 'Best Sellers')], default='AC', max_length=2)),
            ],
        ),
    ]
