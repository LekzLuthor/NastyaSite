# Generated by Django 4.2.11 on 2024-05-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_testquestions_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True, verbose_name='id')),
                ('current_question', models.IntegerField(verbose_name='current_question_number')),
            ],
        ),
    ]
