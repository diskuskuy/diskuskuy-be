# Generated by Django 3.2.18 on 2023-03-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20230310_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialpost',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='nestedreplypost',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='replypost',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
