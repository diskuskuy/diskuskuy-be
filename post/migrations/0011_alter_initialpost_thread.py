# Generated by Django 3.2.18 on 2023-03-10 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_merge_0002_alter_thread_week_0003_initial'),
        ('post', '0010_auto_20230310_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialpost',
            name='thread',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='initial_post', to='forum.thread'),
        ),
    ]
