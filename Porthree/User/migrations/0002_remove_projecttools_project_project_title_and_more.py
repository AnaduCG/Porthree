# Generated by Django 4.2.7 on 2023-12-01 20:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttools',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='projecttools',
            name='user',
            field=models.ForeignKey(default='8ea55a4a-0ce6-4547-9015-519973c7269f', on_delete=django.db.models.deletion.CASCADE, to='User.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='social',
            name='icon',
            field=models.FileField(default='/static/resumes/Hello_everyone.docx', upload_to='static/icons/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='intro',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.BooleanField(blank=True, default=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='posttags',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='projecttools',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='primary_color',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='secondary_color',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='career_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
        migrations.CreateModel(
            name='ProjectSkills',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.project')),
            ],
        ),
    ]