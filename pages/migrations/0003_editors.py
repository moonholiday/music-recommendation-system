# Generated by Django 3.2 on 2022-03-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor_name', models.CharField(max_length=200)),
                ('num_users', models.IntegerField()),
            ],
        ),
    ]
