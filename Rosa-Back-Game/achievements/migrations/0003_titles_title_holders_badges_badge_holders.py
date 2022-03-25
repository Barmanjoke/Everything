# Generated by Django 4.0.3 on 2022-03-24 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0002_remove_badges_association_remove_badges_event_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'titles',
            },
        ),
        migrations.CreateModel(
            name='title_holders',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='achievements.titles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='achievements.users')),
            ],
            options={
                'db_table': 'title_holders',
            },
        ),
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('imageurl', models.URLField()),
                ('description', models.CharField(max_length=300)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='achievements.associations')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='achievements.events')),
            ],
            options={
                'db_table': 'badges',
            },
        ),
        migrations.CreateModel(
            name='badge_holders',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='achievements.badges')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='achievements.users')),
            ],
            options={
                'db_table': 'badge_holders',
            },
        ),
    ]
