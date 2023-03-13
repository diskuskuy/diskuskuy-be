# Generated by Django 3.2.18 on 2023-03-08 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.initialpost')),
                ('post_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
        migrations.CreateModel(
            name='NestedReplyPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('reply_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.replypost')),
            ],
        ),
    ]
