# Generated by Django 4.2 on 2023-05-11 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeGpt_students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=150)),
                ('level', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=1000)),
                ('testcases', models.CharField(max_length=1000)),
                ('expected', models.CharField(max_length=8000)),
            ],
        ),
        migrations.CreateModel(
            name='Students_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refresnce_student_id', models.IntegerField()),
            ],
        ),
    ]
