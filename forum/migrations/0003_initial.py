# Generated by Django 3.2.18 on 2023-03-09 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forum', '0002_delete_resourcetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('mecanism_expectation', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.week')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.TextField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread')),
            ],
        ),
        migrations.CreateModel(
            name='InquiryPhase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('1', 'Phase1'), ('2', 'Phase2'), ('3', 'Phase3'), ('4', 'Phase4')], default='1', max_length=255)),
                ('discussion_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.discussionguide')),
            ],
        ),
        migrations.AddField(
            model_name='discussionguide',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread'),
        ),
    ]
