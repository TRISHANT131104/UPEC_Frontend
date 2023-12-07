# Generated by Django 4.2.7 on 2023-12-05 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_chatmsg_created_at_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='chat_group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.group'),
        ),
        migrations.AddField(
            model_name='project',
            name='workflow',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='team_leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_leaders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatmsg',
            name='created_at_date',
            field=models.CharField(default='5th December 2023', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='chatmsg',
            name='created_at_time',
            field=models.CharField(default='10:58:06 pm', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='created_at_date',
            field=models.CharField(default='5th December 2023', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='created_at_time',
            field=models.CharField(default='10:58:06 pm', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='created_at_date',
            field=models.CharField(default='5th December 2023', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='created_at_time',
            field=models.CharField(default='10:58:06 pm', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.CharField(blank=True, default='5th December 2023 10:58:06 pm', editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.CharField(blank=True, default='5th December 2023 10:58:06 pm', editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.CharField(blank=True, default='5th December 2023 10:58:06 pm', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='learning_resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.learningresource'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.CharField(blank=True, default='5th December 2023 10:58:06 pm', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.CharField(blank=True, default='5th December 2023 10:58:06 pm', editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='projectmembers',
            name='role',
            field=models.CharField(choices=[('Member', 'Member'), ('Mentor', 'Mentor'), ('Client', 'Client'), ('Leader', 'Leader')], default='Member', max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.CharField(blank=True, default='5th December 2023 10:58:06 pm', editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.CharField(blank=True, default='5th December 2023 10:58:06 pm', editable=False, max_length=255, null=True),
        ),
    ]