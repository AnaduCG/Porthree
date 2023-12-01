# Generated by Django 4.2.7 on 2023-12-01 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_posttags_project_user_theme_social_skill_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.RemoveField(
            model_name='projecttools',
            name='project',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.RemoveField(
            model_name='social',
            name='user',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostTags',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectTools',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='Social',
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
