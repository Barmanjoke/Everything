# Generated by Django 4.0.3 on 2022-03-24 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badges',
            name='association',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='event',
        ),
        migrations.RemoveField(
            model_name='title_holders',
            name='title',
        ),
        migrations.RemoveField(
            model_name='title_holders',
            name='user',
        ),
        migrations.DeleteModel(
            name='badge_holders',
        ),
        migrations.DeleteModel(
            name='Badges',
        ),
        migrations.DeleteModel(
            name='title_holders',
        ),
        migrations.DeleteModel(
            name='Titles',
        ),
    ]