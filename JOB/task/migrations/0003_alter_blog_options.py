# Generated by Django 4.1.2 on 2022-10-20 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_delete_user_remove_search_calendar_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['created_date']},
        ),
    ]
