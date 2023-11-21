# Generated by Django 4.2.7 on 2023-11-16 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charName', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('charClass', models.CharField(max_length=20)),
                ('support', models.CharField(max_length=20)),
                ('goodOrBad', models.CharField(max_length=20)),
                ('weapons', models.CharField(max_length=20)),
                ('otherOne', models.CharField(max_length=20)),
                ('otherTwo', models.CharField(max_length=20)),
                ('otherThree', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
