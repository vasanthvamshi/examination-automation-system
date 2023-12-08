# Generated by Django 2.2.3 on 2020-07-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200708_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarksModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=500)),
                ('marks', models.CharField(default='', max_length=500)),
            ],
            options={
                'db_table': 'MarksTable',
            },
        ),
    ]