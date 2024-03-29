# Generated by Django 3.2.18 on 2023-03-10 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_initial'),
        ('post', '0009_auto_20230310_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialpost',
            name='thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='initial_post', to='forum.thread'),
        ),
        migrations.AlterField(
            model_name='nestedreplypost',
            name='reply_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nested_reply_post', to='post.replypost'),
        ),
        migrations.AlterField(
            model_name='replypost',
            name='initial_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_post', to='post.initialpost'),
        ),
    ]
